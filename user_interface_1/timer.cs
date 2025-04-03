using UnityEngine;
using TMPro;

public class TimerScript : MonoBehaviour
{
    public TextMeshProUGUI timerText;  // Reference to TMP Text
    private float elapsedTime = 0f;
    private bool isRunning = true;
    private float maxTime = 12 * 60; // 12 minutes in seconds

    void Update()
    {
        if (isRunning)
        {
            elapsedTime += Time.deltaTime; // Increment timer

            if (elapsedTime >= maxTime)
            {
                elapsedTime = maxTime; // Cap at 12:00
                isRunning = false;
            }

            UpdateTimerDisplay();
        }
    }

    void UpdateTimerDisplay()
    {
        if (timerText != null)
        {
            int minutes = Mathf.FloorToInt(elapsedTime / 60);
            int seconds = Mathf.FloorToInt(elapsedTime % 60);
            timerText.text = $"{minutes}:{seconds:00}"; // Format as MM:SS
        }
        else
        {
            Debug.LogWarning("TimerScript: timerText is not assigned!");
        }
    }
}
