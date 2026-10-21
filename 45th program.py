from datetime import datetime

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] {self.sender.username}: {self.content}"

class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, chat_room, content):
        if self in chat_room.members:
            chat_room.broadcast(self, content)
        else:
            print(f"⚠️ {self.username} cannot send messages; they are not in the room.")

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.members = []
        self.history = []

    def add_user(self, user):
        if user not in self.members:
            self.members.append(user)
            print(f"✅ {user.username} joined {self.room_name}.")
        
    def remove_user(self, user):
        if user in self.members:
            self.members.remove(user)
            print(f"🚪 {user.username} left {self.room_name}.")

    def broadcast(self, sender, content):
        new_msg = Message(sender, content)
        self.history.append(new_msg)
        print(f"📢 New message in {self.room_name}: {new_msg}")

    def view_history(self):
        print(f"\n--- Chat History for {self.room_name} ---")
        if not self.history:
            print("No messages yet.")
        for msg in self.history:
            print(msg)
        print("------------------------------\n")
   #      --- Example Usage ---

# 1. Initialize Room and Users
lounge = ChatRoom("The Lounge")
alice = User("Alice")
bob = User("Bob")

# 2. Users Join
lounge.add_user(alice)
lounge.add_user(bob)

# 3. Sending Messages
alice.send_message(lounge, "Hi everyone!")
bob.send_message(lounge, "Hey Alice, how are you?")

# 4. View History
lounge.view_history()

# 5. User Leaves
lounge.remove_user(alice)
alice.send_message(lounge, "Can I still talk?") # Should fail