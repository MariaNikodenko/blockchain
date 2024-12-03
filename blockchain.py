import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index  # Номер блоку
        self.timestamp = datetime.datetime.now()  # Дата створення
        self.data = data  # Дані, які зберігаються
        self.previous_hash = previous_hash  # Хеш попереднього блоку
        self.hash = self.calculate_hash()  # Поточний хеш

    def calculate_hash(self):
        # Хешуємо дані блоку
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Ланцюг починається з "генезис-блоку"

    def create_genesis_block(self):
        # Створюємо перший блок у ланцюгу
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        # Додаємо новий блок до ланцюга
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Перевіряємо цілісність ланцюга
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Перевіряємо, чи співпадають хеші
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
# Тестування
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Додаємо блоки
    my_blockchain.add_block("Player1 scored 100 points")
    my_blockchain.add_block("Player2 reached level 5")
    my_blockchain.add_block("Player3 found a rare item")

    # Перевіряємо ланцюг
    print("Is blockchain valid?", my_blockchain.is_chain_valid())

    # Виводимо інформацію про блоки
    for block in my_blockchain.chain:
        print(f"Block {block.index} | Data: {block.data} | Hash: {block.hash}")
