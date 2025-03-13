using UnityEngine;

public class SpawningRespawning : MonoBehaviour
{
    public GameObject playerPrefab;  // Assign Player Prefab in Inspector
    public Transform respawnPoint;   // Assign Empty GameObject (RespawnPoint) in Inspector
    private GameObject currentPlayer; // Store reference to the player

    void Start()
    {
        currentPlayer = GameObject.FindGameObjectWithTag("Player"); // Find existing player
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.B) && currentPlayer != null)
        {
            RespawnPlayer();
        }
    }

    void RespawnPlayer()
    {
        Destroy(currentPlayer); // Destroy current player
        currentPlayer = Instantiate(playerPrefab, respawnPoint.position, Quaternion.identity); // Spawn new player
    }
}
