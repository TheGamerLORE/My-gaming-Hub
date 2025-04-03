using UnityEngine;
using UnityEngine.UI;
using System.Collections;

namespace YourGameNamespace
{
    public class HealthBar : MonoBehaviour
    {
        public Slider hpBar;  
        public int maxHP = 20; 
        private int currentHP;

        public delegate void HealthChanged(int currentHP);
        public event HealthChanged OnHealthChanged;

        void Start()
        {
            if (hpBar == null)
            {
                Debug.LogWarning("HealthBar: hpBar is not assigned in the Inspector!");
                return;
            }

            currentHP = maxHP; 
            UpdateHPBar();
        }

        public void TakeDamage(int damage)
        {
            currentHP -= damage;
            currentHP = Mathf.Clamp(currentHP, 0, maxHP); 
            UpdateHPBar();
        }

        public void Heal(int amount)
        {
            currentHP += amount;
            currentHP = Mathf.Clamp(currentHP, 0, maxHP);
            UpdateHPBar();
        }

        void UpdateHPBar()
        {
            if (hpBar != null)
            {
                StartCoroutine(SmoothHPBarChange((float)currentHP / maxHP));
            }

            OnHealthChanged?.Invoke(currentHP); // Notify listeners
        }

        IEnumerator SmoothHPBarChange(float targetValue)
        {
            float duration = 0.3f;
            float startValue = hpBar.value;
            float elapsed = 0f;

            while (elapsed < duration)
            {
                elapsed += Time.deltaTime;
                hpBar.value = Mathf.Lerp(startValue, targetValue, elapsed / duration);
                yield return null;
            }

            hpBar.value = targetValue;
        }

        public int CurrentHP => currentHP; // Read-only property
    }
}