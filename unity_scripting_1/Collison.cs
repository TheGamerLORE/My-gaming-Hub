/*using UnityEngine;

public class Collison : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    { using UnityEngine;

public class TokenPickup : MonoBehaviour
{
    public string playerTag = "Player"; // Tag to identify the player
    public AudioClip pickupSound; // Optional pickup sound
    public ParticleSystem pickupEffect; // Optional effect on pickup

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag(playerTag))
        {
            ApplyUpgrade(other.gameObject); // Apply the upgrade effect
            PlayEffects();
            Destroy(gameObject); // Remove the token after pickup
        }
    }

    void ApplyUpgrade(GameObject player)
    {
        // You can modify this to call your upgrade system
        Debug.Log("Upgrade applied to: " + player.name);
    }

    void PlayEffects()
    {
        if (pickupSound)
            AudioSource.PlayClipAtPoint(pickupSound, transform.position);

        if (pickupEffect)
            Instantiate(pickupEffect, transform.position, Quaternion.identity);
    }
}

        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
*/