namespace MathGame;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }

    // Generate math exercises for add, subtract, multiply, and division operations

    // - Generate random numbers
    static Tuple<int, int> GenerateRandomNumberPair()
    {
        Random random = new();
        int num1 = random.Next(1, 100);
        int num2 = random.Next(1, 100);

        return (num1, num2);
    }

    static CheckAnswer(Tuple<int, int> exerciseNums, Operator op, int answer)
    {
        int correctAnswer = 0;

        switch (op)
        {
            case Operator.ADD:
                correctAnswer = exerciseNums.Item1 + exerciseNums.Item2;
                break;
            case Operator.SUBTRACT:
                correctAnswer = exerciseNums.Item1 - exerciseNums.Item2;
                break;
            case Operator.MULTIPLY:
                correctAnswer = exerciseNums.Item1 * exerciseNums.Item2;
                break;
            case Operator.DIVIDE:
                correctAnswer = exerciseNums.Item1 / exerciseNums.Item2;
                break;
            default:
                throw new ArgumentException("argument must be one of four arithmetic operator types!");
            
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
