# MSCS631_Lab_2
UDP Pinger


Implement the UDP Ping Client – client-side Python script that communicates with the given UDP ping server.

Run & Verify the Client – execute the client code and take screenshots of successful pings and timeouts.

screenshots at the client verifying that your ping program works as required. 

![](./screenshots/)


# Experience
Implementing the UDP Pinger was an insightful experience, demonstrating the differences between UDP and TCP. Unlike TCP, UDP does not guarantee packet delivery, which was evident as some packets were lost due to simulated conditions. Running the server and client on localhost allowed for quick debugging and testing of real-time round-trip times (RTT). By using Python’s socket module, I was able to send and receive messages efficiently, observing how some packets were lost while others successfully returned echoed responses.

# Challenges
One of the challenges was ensuring the timeout mechanism worked correctly. If the client waited indefinitely, it would hang when no response was received. Implementing socket.settimeout(1) ensured that unresponsive requests were handled properly. 

Additionally, since UDP does not establish a persistent connection, handling packet loss required retries and checking response consistency. Another challenge was running the server and client simultaneously while ensuring the server properly simulated packet loss for realistic network conditions.

