using UnityEngine;

public class Bob : MonoBehaviour
{
    // Public variables for inputs, configurable in the Inspector
    public int number = 500;
    public int num1 = 0; // Input through the Inspector or via script
    public int num2 = 0;

    // Start is called before the first frame update
    void Start()
    {
        // Check if number is greater than 100
        if (number > 100)
        {
            Debug.Log("The number is bigger than 100");
        }
        else
        {
            Debug.Log("The number is smaller than 100");
        }

        // Perform addition
        int result = AddNumbers(num1, num2);
        Debug.Log($"The sum of {num1} and {num2} is {result}.");
        
        // array = a variable that can store multiple values. fixed sizs

        string[] cars = {"BMW", "Mustang", "Corvette"};

        cars[0] = "Tesla";

        for (int i = 0; i < cars.Length; i++)
        {
            Debug.Log(cars[i]);
        }


  }  // Custom function to log a message
    public void CustomFunction()
    {
        Debug.Log("This function has been called");
    }

    // Function to add two numbers
    static int AddNumbers(int a, int b)
    {
        return a + b;
    }
}



   




 