import kotlin.random.Random
import kotlin.random.nextInt

class Node<T : Comparable<T>>(val value: T?, var next: Node<T>? = null, var dense: Node<T>? = null)

class SkipList<T : Comparable<T>>(val promoteProbability: Double = 0.5) {
    private var size = 0
    private val roots = mutableListOf<Node<T>>(Node(null)) // roots从底层到顶层

    fun size() = size

    fun toList(): List<T> {
        val list = mutableListOf<T>()
        var node = roots[0].next
        while (node != null) {
            list.add(node.value!!)
            node = node.next
        }
        return list
    }

    override fun toString() = this.toList().toString()

    fun contains(value: T): Boolean {
        val memoryNodes = find(value)
        if (memoryNodes.last().next!!.value == value)
            return true
        return false
    }

    private fun insertNode(newNode: Node<T>, prev: Node<T>) {
        val originalNext = prev.next
        newNode.next = originalNext
        prev.next = newNode
    }

    private fun removeNode(toRemove: Node<T>, prev: Node<T>) {
        prev.next = toRemove.next
    }

    private fun find(value: T): MutableList<Node<T>> {
        val memoryNodes = mutableListOf<Node<T>>()

        var i = roots.size - 1
        var currentNode = roots[i]

        // 在高层搜索
        while (i > 0) {
            while (currentNode.next != null && value > currentNode.next!!.value!!) {
                currentNode = currentNode.next!!
            }
            memoryNodes.add(currentNode)
            currentNode = currentNode.dense!!
            i -= 1
        }

        // 在底层搜索
        while (currentNode.next != null && value > currentNode.next!!.value!!) {
            currentNode = currentNode.next!!
        }
        memoryNodes.add(currentNode)

        return memoryNodes
    }

    fun add(value: T) {
        size += 1

        val memoryNodes = find(value)

        // 插入底层节点
        val newNode = Node<T>(value)
        insertNode(newNode, memoryNodes.removeAt(memoryNodes.lastIndex))
        var currentNode = newNode

        // 随机决定是否向上层添加相同值节点
        var currentLevel = 1
        while (Random.nextDouble() < promoteProbability) {
            val upperNode = Node<T>(value, dense = currentNode)

            currentLevel += 1
            if (currentLevel <= roots.size) { // 不用加新的层
                insertNode(upperNode, memoryNodes.removeAt(memoryNodes.lastIndex))
            } else {
                val newRootNode = Node<T>(null, next = upperNode, dense = roots[currentLevel - 2])
                roots.add(newRootNode)
                break
            }
            currentNode = upperNode // 继续往上层添加
        }
    }

    fun remove(value: T) {
        if (!this.contains(value))
            throw IllegalStateException("$value not in this skip list")

        val memoryNodes = find(value)
        for (node in memoryNodes) {
            if (node.next != null && node.next!!.value == value)
                removeNode(node.next!!, node)
        }
        size -= 1

        // 检查是否有层被清空
        for (i in (roots.size - 1) downTo 1)
            if (roots[i].next == null)
                roots.removeAt(i)
    }
}


fun main() {
    val MAX = 999999999
    val LENGTH = 100000

    val skipList = SkipList<Int>(promoteProbability = 0.5)

    val testData = List(LENGTH) { Random.nextInt(1..MAX) }

    val t1 = System.currentTimeMillis()
    for (num in testData)
        skipList.add(num)
    val t2 = System.currentTimeMillis()

    val testDataSorted = testData.sorted()
    println("add time cost ${t2 - t1} ms, correct: ${skipList.toList() == testDataSorted}")

    val dataToRemove = testData.subList(0, testData.size / 2) // 抽前面一半的数来删除
    val t3 = System.currentTimeMillis()
    for (num in dataToRemove)
        skipList.remove(num)
    val t4 = System.currentTimeMillis()

    val testDataRemainingSorted = testData.subList(testData.size / 2, testData.size).sorted()
    println("remove time cost ${t4 - t3} ms, correct: ${skipList.toList() == testDataRemainingSorted}")
}
