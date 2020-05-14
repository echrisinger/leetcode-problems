from queue import PriorityQueue
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.action_keys = {}
        self.key_action = {}
        self.action_counter = 0
        self.min_action = 0

    def get(self, key: int) -> int:
        self.action_counter += 1
        res = -1
        if key in self.values:
            self.update_action(key)
            res = self.values[key]
        
        return res
        
    def put(self, key: int, value: int) -> None:
        self.action_counter += 1
        if key in self.values:
            self.values[key] = value
            self.update_action(key)
        else:
            if len(self.values) >= self.capacity:
                # remove the oldest value
                # find oldest value as could be out of date due to calls to get
                while self.min_action not in self.action_keys:
                    self.min_action += 1
                
                key_to_remove = self.action_keys[self.min_action]
                del self.action_keys[self.min_action]
                del self.key_action[key_to_remove]
                del self.values[key_to_remove]
                self.min_action += 1
                
            self.values[key] = value
            self.action_keys[self.action_counter] = key
            self.key_action[key] = self.action_counter

            
    def update_action(self, key: int):
        old_action = self.key_action[key]
        del self.action_keys[old_action]
        
        self.action_keys[self.action_counter] = key
        self.key_action[key] = self.action_counter
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

