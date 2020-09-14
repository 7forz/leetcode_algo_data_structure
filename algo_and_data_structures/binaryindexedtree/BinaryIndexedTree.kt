import kotlin.random.Random
import kotlin.random.nextInt

class BinaryIndexedTree(list: List<Int>) {
    private val array = MutableList(list.size + 1) { 0 }

    init {
        /** initialize in O(n log n) */
        // for ((i, value) in list.withIndex())
        //    update(i, value)

        /** initialize in O(n) */
        for ((i, value) in list.withIndex())
            array[i+1] = value
        for (index in 1 until array.size) {
            val j = index + lsb(index)
            if (j < array.size)
                array[j] += array[index]
        }
    }

    private fun lsb(n: Int) = n and (-n) // bitwise and

    private fun prefixSum(index: Int): Int {
        var index = index + 1
        var result = 0
        while (index != 0) {
            result += this.array[index]
            index -= lsb(index)
        }
        return result
    }

    fun rangeSum(start: Int, end: Int) = prefixSum(end) - prefixSum(start - 1)

    fun update(index: Int, delta: Int) {
        var index = index + 1
        while (index < this.array.size) {
            this.array[index] += delta
            index += lsb(index)
        }
    }
}


fun main() {
    val MAX = 10000
    val LENGTH = 1000

    val testData = MutableList(LENGTH) { Random.nextInt(1..MAX) }

    val binaryIndexedTree = BinaryIndexedTree(testData)

    println("the sum of [12, 345] is ${testData.subList(12, 346).reduce { a, b -> a + b }} (by simple addition)")
    println("the sum of [12, 345] is ${binaryIndexedTree.rangeSum(12, 345)} (by binary indexed tree)")

    // 随便找10个元素，各加上随机值
    for (i in 1..10) {
        val randomIndex = Random.nextInt(0 until LENGTH)
        val randomDelta = Random.nextInt(1..MAX)
        testData[randomIndex] += randomDelta
        binaryIndexedTree.update(randomIndex, randomDelta)
    }

    println("\nafter updating some data")
    println("the sum of [123, 666] is ${testData.subList(123, 667).reduce { a, b -> a + b }} (by simple addition)")
    println("the sum of [123, 666] is ${binaryIndexedTree.rangeSum(123, 666)} (by binary indexed tree)")
}
