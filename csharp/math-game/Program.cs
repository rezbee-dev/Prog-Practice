namespace MathGame;

class Program
{
    static void Main(string[] args)
    {
        int result = ReadAnswer();
        Console.WriteLine($"Result: {result}");
        // Console.WriteLine("Testing 'GenerateRandomNumberPair()'");
        // for (int i = 0; i < 5; i++)
        // {
        //     Console.WriteLine($"#{i+1} - {GenerateRandomNumberPairForDivision()}");
        // }
    }

    // Generate math exercises for add, subtract, multiply, and division operations
    static (int, int) GenerateRandomNumberPair()
    {

        Random random = new();
        int num1 = random.Next(1, 100);
        int num2 = random.Next(1, 100);

        return (Math.Max(num1, num2), Math.Min(num1, num2));
    }

    static (int, int) GenerateRandomNumberPairForDivision()
    {
        Random random = new();
        int num1 = random.Next(1, 100);
        int factor = random.Next(2, 10);

        return (num1 * factor, num1);
    }

    static bool CheckAnswer((int,int) exerciseNums, Operator op, int answer)
    {
        int correctAnswer;

        correctAnswer = op switch
        {
            Operator.ADD => exerciseNums.Item1 + exerciseNums.Item2,
            Operator.SUBTRACT => exerciseNums.Item1 - exerciseNums.Item2,
            Operator.MULTIPLY => exerciseNums.Item1 * exerciseNums.Item2,
            Operator.DIVIDE => exerciseNums.Item1 / exerciseNums.Item2,
            _ => throw new ArgumentException("argument must be one of four arithmetic operator types!"),
        };

        return correctAnswer == answer;
    }

    // Handle user input
    static int ReadAnswer()
    {
        while (true)
        {
            Console.Write("Answer: ");
            string? answer = Console.ReadLine();
            if(int.TryParse(answer, out int result))
            {
                return result;
            }
        }
    }

    enum Operator
    {
        ADD,
        SUBTRACT,
        MULTIPLY,
        DIVIDE
    }
}
