namespace PracticeApp;

public class Program
{
    public static void Main()
    {
        // Sanity check
        Console.WriteLine("Hello, C#!");

        // Test: Output Param
        int ans;
        AddUsingOutParam(90, 90, out ans);
        Console.WriteLine($"Ans: {ans}");
        
        // Test Value Type Args
        // int x = 5, y = 10;
        // Console.WriteLine($"Before - x: {x}, y: {y}");
        // Add(x, y);
        // Console.WriteLine($"After - x: {x}, y: {y}");
    }

    // Value Type Arguments demo
    static int Add(int x, int y)
    {
        int ans = x + y;

        // x & y changes should not be seen in the caller function
        x = 10000;
        y = 88888;

        return ans;
    }

    // Output Param Demo
    static void AddUsingOutParam(int x, int y, out int ans)
    {
        ans = x + y;
    }
}