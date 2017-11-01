public class Main
{

    public static void main(String[] args)
    {
        System.out.println("FileLoadingtest");
        BinaryHeap<Integer> mMaxheap = new BinaryHeap<Integer>(BinaryHeap.HeapType.MAXHEAP);
        BinaryHeap<String> mMinheap = new BinaryHeap<String>(BinaryHeap.HeapType.MINHEAP);

        WordCounter count = new WordCounter("warandpeace.txt",11);
        BruteForce brute = new BruteForce("warandpeace.txt",10);

        System.out.println("HeapMethodstest" + " \n" + "MaxHeap");

        mMaxheap.push(50);
        mMaxheap.push(20);
        mMaxheap.push(27);
        mMaxheap.push(77);
        mMaxheap.push(65);
        mMaxheap.push(5);
        mMaxheap.push(7);
        mMaxheap.push(89);
        mMaxheap.push(8);
        mMaxheap.push(35);
        mMaxheap.push(56);
        mMaxheap.push(90);
        mMaxheap.push(88);
        System.out.println(mMaxheap.getHeap());
        System.out.println(mMaxheap.size());
        mMaxheap.pop();
        System.out.println(mMaxheap.getHeap());

        System.out.println("MinHeap");

        mMinheap.push("a");
        mMinheap.push("b");
        mMinheap.push("c");
        mMinheap.push("g");
        mMinheap.push("h");
        mMinheap.push("o");
        System.out.println(mMinheap.getHeap());
        System.out.println(mMaxheap.size());
        mMinheap.pop();
        mMinheap.pop();
        System.out.println(mMinheap.getHeap());











    }



}
