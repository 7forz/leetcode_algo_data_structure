import java.util.*;
import java.util.stream.Collectors;

class Node<T extends Comparable<T>> {
    private final T value;
    private Node<T> next;
    private Node<T> dense;

    public T getValue() {
        return value;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public Node<T> getDense() {
        return dense;
    }

    public void setDense(Node<T> dense) {
        this.dense = dense;
    }

    public Node(T value) {
        this.value = value;
    }
}

public class SkipList<T extends Comparable<T>> {
    private final double promoteProbability;
    private int size = 0;
    private final List<Node<T>> roots;

    public SkipList() {
        roots = new LinkedList<>();
        roots.add(new Node<>(null));
        promoteProbability = 0.5;
    }

    public SkipList(double promoteProbability) {
        roots = new LinkedList<>();
        roots.add(new Node<>(null));
        this.promoteProbability = promoteProbability;
    }

    public int getSize() {
        return size;
    }

    public List<T> toList() {
        List<T> list = new ArrayList<>();
        Node<T> node = roots.get(0).getNext();
        while (node != null) {
            list.add(node.getValue());
            node = node.getNext();
        }
        return list;
    }

    @Override
    public String toString() {
        return toList().toString();
    }

    boolean contains(T value) {
        List<Node<T>> memoryNodes = find(value);
        return memoryNodes.get(memoryNodes.size() - 1).getNext().getValue().equals(value);
    }

    private void insertNode(Node<T> newNode, Node<T> prev) {
        Node<T> originalNext = prev.getNext();
        newNode.setNext(originalNext);
        prev.setNext(newNode);
    }

    private void removeNode(Node<T> toRemove, Node<T> prev) {
        prev.setNext(toRemove.getNext());
    }

    private List<Node<T>> find(T value) {
        List<Node<T>> memoryNodes = new LinkedList<>();

        int i = roots.size() - 1;
        Node<T> currentNode = roots.get(i);

        // 在高层搜索
        while (i > 0) {
            while (currentNode.getNext() != null && value.compareTo(currentNode.getNext().getValue()) > 0) {
                currentNode = currentNode.getNext();
            }
            memoryNodes.add(currentNode);
            currentNode = currentNode.getDense();
            i -= 1;
        }

        // 在底层搜索
        while (currentNode.getNext() != null && value.compareTo(currentNode.getNext().getValue()) > 0) {
            currentNode = currentNode.getNext();
        }
        memoryNodes.add(currentNode);

        return memoryNodes;
    }

    public void add(T value) {
        size += 1;

        List<Node<T>> memoryNodes = find(value);

        // 插入底层节点
        Node<T> newNode = new Node<>(value);
        insertNode(newNode, memoryNodes.remove(memoryNodes.size() - 1));
        Node<T> currentNode = newNode;

        // 随机决定是否向上层添加相同值节点
        int currentLevel = 1;
        while (Math.random() < promoteProbability) {
            Node<T> upperNode = new Node<>(value);
            upperNode.setDense(currentNode);

            currentLevel += 1;
            if (currentLevel <= roots.size()) {
                insertNode(upperNode, memoryNodes.remove(memoryNodes.size() - 1));
            } else {
                Node<T> newRootNode = new Node<>(null);
                newRootNode.setNext(upperNode);
                newRootNode.setDense(roots.get(currentLevel - 2));
                roots.add(newRootNode);
                break;
            }
            currentNode = upperNode;
        }
    }

    public void remove(T value) {
        if (!this.contains(value))
            throw new IllegalStateException(value.toString() + " not in this skip list");

        List<Node<T>> memoryNodes = find(value);
        for (Node<T> node : memoryNodes) {
            if (node.getNext() != null && node.getNext().getValue().equals(value))
                removeNode(node.getNext(), node);
        }
        size -= 1;

        // 检查是否有层被清空
        for (int i = roots.size() - 1; i >= 1; i--) {
            if (roots.get(i).getNext() == null)
                roots.remove(i);
        }
    }

    public static void main(String[] args) {
        int MAX = 999999999;
        int LENGTH = 100000;

        SkipList<Integer> skipList = new SkipList<>(0.5);

        Random r = new Random();
        List<Integer> testData = new ArrayList<>(LENGTH);
        for (int i = 0; i < LENGTH; i++) {
            testData.add(r.nextInt(MAX));
        }

        Long t1 = System.currentTimeMillis();
        for (Integer num : testData)
            skipList.add(num);
        Long t2 = System.currentTimeMillis();

        List<Integer> testDataSorted = testData.stream().sorted().collect(Collectors.toList());
        System.out.println("add time cost " + (t2 - t1) + "ms, correct: " + (skipList.toList().equals(testDataSorted)));

        List<Integer> dataToRemove = testData.subList(0, testData.size() / 2);
        Long t3 = System.currentTimeMillis();
        for (Integer num : dataToRemove)
            skipList.remove(num);
        Long t4 = System.currentTimeMillis();

        List<Integer> testDataRemainingSorted = testData.subList(testData.size() / 2, testData.size())
                .stream().sorted().collect(Collectors.toList());
        System.out.println("remove time cost " + (t4 - t3) + "ms, correct: " + (skipList.toList().equals(testDataRemainingSorted)));
    }
}
