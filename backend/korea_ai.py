import subprocess
import json

def stream_chat_response(prompt):
    """
    Sends a prompt to the API and streams the response in real-time.

    :param prompt: The user input to be sent to the API.
    :return: None
    """
    
    # Prepare the curl command
    curl_command = [
        "curl",
        "-X", "POST", "https://bible.us.gaianet.network/v1/chat/completions",
        "-H", "accept: application/json",
        "-H", "Content-Type: application/json",
        "-d", json.dumps({
            "messages": [
                {"role": "system", "content": "You are very elite person,you know that InspireEd: A blockchain-based crowdfunding platform for students, teachers, any professional into reasearch and project to get funded by public worldwide. It opens a gate to get funded from anywhere around the world and also increases awareness of web3, also InspireEd: A blockchain-based crowdfunding platform for students, teachers, any professional into reasearch and project to get funded by public worldwide -> Purpose: Supports academic projects and research. -> Built on: A custom blockchain called EduChain. -> Powered by: InspireEd Tokens. -> Connects: Innovative students and teachers with backers globally. -> Funding: For diverse academic projects, from student experiments to educator research. -> Crypto Wallet Integration: Enables easy and transparent funding. -> Security: Blockchain ensures all contributions are securely tracked. -> Global Community: Dedicated to advancing knowledge through decentralized support. -> Impact: Contributors help fuel discovery and empower future innovators with EduTokens. You help people with other queries too."},
                {"role": "user", "content": prompt}
            ],
            "stream": True
        })
    ]

    # Execute the curl command and stream the output
    process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    full_content = ""
    try:
        # Read the output line by line
        for line in process.stdout:
            if line.startswith("data:"):
                # Extract the JSON part after "data: "
                json_data = line[5:].strip()
                if json_data:  # Ensure it's not empty
                    try:
                        # Parse the JSON
                        parsed_data = json.loads(json_data)
                        # Extract and print the content value
                        content_value = parsed_data["choices"][0]["delta"]["content"]
                        full_content += content_value
                        print(content_value, end='', flush=True)  # Print without newline, flush output
                        # return "jesus loves you"
                    except (json.JSONDecodeError, KeyError):
                        pass  # Handle errors in parsing without breaking the stream
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        process.stdout.close()
        process.wait()
        return full_content


if __name__ == "__main__":
    print("ASK/PROMPT :")
    user_prompt = input()  # Ask the user for input
    stream_chat_response(user_prompt)  # Call the function
