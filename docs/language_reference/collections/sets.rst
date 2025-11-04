Sets
====

Sets are unordered collections of unique elements, ideal for membership testing, elimination of duplicates, and mathematical set operations.

Set Creation
------------

Basic Set Creation
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Empty set
   empty_set = set();
   
   # From list (removes duplicates)
   numbers = set([1, 2, 2, 3, 3, 3]);  # {1, 2, 3}
   colors = {"red", "green", "blue", "green"};  # {"red", "green", "blue"}
   
   # From range
   evens = set(0..10, 2);  # {0, 2, 4, 6, 8, 10}
   
   # Set comprehension
   squares = {x * x for x in 1..5};  # {1, 4, 9, 16, 25}

Set Operations
--------------

Basic Operations
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   a = {1, 2, 3, 4, 5};
   b = {4, 5, 6, 7, 8};
   
   # Union
   union = a.union(b);        # {1, 2, 3, 4, 5, 6, 7, 8}
   union_alt = a | b;         # Same as union
   
   # Intersection
   intersection = a.intersect(b);  # {4, 5}
   intersection_alt = a & b;       # Same as intersect
   
   # Difference
   difference = a.difference(b);   # {1, 2, 3}
   difference_alt = a - b;         # Same as difference
   
   # Symmetric difference
   sym_diff = a.symmetric_difference(b);  # {1, 2, 3, 6, 7, 8}
   sym_diff_alt = a ^ b;                  # Same as symmetric_difference

Set Relations
~~~~~~~~~~~~~

.. code-block:: symbolic

   a = {1, 2, 3};
   b = {1, 2, 3, 4, 5};
   c = {4, 5, 6};
   
   # Subset checks
   is_subset = a.is_subset(b);      # true
   is_proper_subset = a.is_proper_subset(b);  # true
   is_superset = b.is_superset(a);  # true
   
   # Disjoint check
   are_disjoint = a.is_disjoint(c);  # true

Set Methods
-----------

Basic Methods
~~~~~~~~~~~~~

.. code-block:: symbolic

   numbers = {1, 2, 3};
   
   # Add elements
   numbers.add(4);           # {1, 2, 3, 4}
   numbers.add(2);           # No change (already exists)
   
   # Remove elements
   numbers.remove(3);        # {1, 2, 4}
   numbers.discard(5);       # No error if not present
   popped = numbers.pop();   # Remove and return arbitrary element
   
   # Clear set
   numbers.clear();          # set()
   
   # Copy set
   copy = numbers.copy();    # New set with same elements

Set Properties
~~~~~~~~~~~~~~

.. code-block:: symbolic

   primes = {2, 3, 5, 7, 11};
   
   size = primes.length();      # 5
   is_empty = primes.is_empty(); # false
   
   # Membership testing
   contains_3 = 3 in primes;    # true
   contains_4 = 4 in primes;    # false

Practical Examples
------------------

Data Deduplication
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn remove_duplicates(data) {
       return set(data).list();
   }
   
   fn find_unique_elements(list1, list2) {
       set1 = set(list1);
       set2 = set(list2);
       
       # Elements in list1 but not in list2
       only_in_list1 = set1 - set2;
       
       # Elements in list2 but not in list1
       only_in_list2 = set2 - set1;
       
       # Common elements
       common = set1 & set2;
       
       return {
           unique_to_first: only_in_list1.list(),
           unique_to_second: only_in_list2.list(),
           common: common.list()
       };
   }

Tagging System
~~~~~~~~~~~~~~

.. code-block:: symbolic

   class TagSystem {
       items = {};
       
       fn add_tags(item_id, tags) {
           if item_id not in self.items {
               self.items[item_id] = set();
           }
           self.items[item_id].update(tags);
       }
       
       fn remove_tags(item_id, tags) {
           if item_id in self.items {
               self.items[item_id].difference_update(tags);
           }
       }
       
       fn find_items_with_all_tags(required_tags) {
           required_set = set(required_tags);
           matching_items = [];
           
           for item_id, tags in self.items.entries() {
               if required_set.is_subset(tags) {
                   matching_items.append(item_id);
               }
           }
           
           return matching_items;
       }
       
       fn find_related_items(item_id, min_common_tags = 1) {
           if item_id not in self.items {
               return [];
           }
           
           item_tags = self.items[item_id];
           related = [];
           
           for other_id, other_tags in self.items.entries() {
               if other_id != item_id {
                   common_tags = item_tags & other_tags;
                   if common_tags.length() >= min_common_tags {
                       related.append({
                           "item_id": other_id,
                           "common_tags": common_tags.list(),
                           "score": common_tags.length()
                       });
                   }
               }
           }
           
           return related.sorted((a, b) => b.score - a.score);
       }
   }

Permission System
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class PermissionManager {
       user_roles = {};      # user_id -> set of roles
       role_permissions = {}; # role -> set of permissions
       
       fn assign_role(user_id, role) {
           if user_id not in self.user_roles {
               self.user_roles[user_id] = set();
           }
           self.user_roles[user_id].add(role);
       }
       
       fn remove_role(user_id, role) {
           if user_id in self.user_roles {
               self.user_roles[user_id].remove(role);
           }
       }
       
       fn user_has_permission(user_id, permission) {
           if user_id not in self.user_roles {
               return false;
           }
           
           user_roles = self.user_roles[user_id];
           user_permissions = set();
           
           for role in user_roles {
               if role in self.role_permissions {
                   user_permissions.update(self.role_permissions[role]);
               }
           }
           
           return permission in user_permissions;
       }
       
       fn get_users_with_permission(permission) {
           users_with_permission = [];
           
           for user_id, roles in self.user_roles.entries() {
               user_permissions = set();
               for role in roles {
                   if role in self.role_permissions {
                       user_permissions.update(self.role_permissions[role]);
                   }
               }
               
               if permission in user_permissions {
                   users_with_permission.append(user_id);
               }
           }
           
           return users_with_permission;
       }
   }

Graph Algorithms
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Graph {
       adjacency = {};  # node -> set of neighbors
       
       fn add_edge(node1, node2) {
           if node1 not in self.adjacency {
               self.adjacency[node1] = set();
           }
           if node2 not in self.adjacency {
               self.adjacency[node2] = set();
           }
           
           self.adjacency[node1].add(node2);
           self.adjacency[node2].add(node1);
       }
       
       fn find_connected_component(start_node) {
           if start_node not in self.adjacency {
               return set();
           }
           
           visited = set();
           stack = [start_node];
           
           while stack.length() > 0 {
               node = stack.pop();
               if node not in visited {
                   visited.add(node);
                   # Add all unvisited neighbors
                   for neighbor in self.adjacency[node] {
                       if neighbor not in visited {
                           stack.append(neighbor);
                       }
                   }
               }
           }
           
           return visited;
       }
       
       fn find_all_connected_components() {
           visited = set();
           components = [];
           
           for node in self.adjacency.keys() {
               if node not in visited {
                   component = self.find_connected_component(node);
                   components.append(component);
                   visited.update(component);
               }
           }
           
           return components;
       }
   }

Data Analysis
~~~~~~~~~~~~~

.. code-block:: symbolic

   fn analyze_customer_segments(customers) {
       # Extract all unique attributes
       all_interests = set();
       all_locations = set();
       all_age_groups = set();
       
       for customer in customers {
           all_interests.update(customer.interests);
           all_locations.add(customer.location);
           all_age_groups.add(customer.age_group);
       }
       
       # Find popular combinations
       interest_combinations = {};
       for customer in customers {
           # Create a frozen set (tuple of sorted interests) as key
           key = tuple(customer.interests.sorted());
           interest_combinations[key] = (interest_combinations[key] or 0) + 1;
       }
       
       # Find exclusive interests (only one customer has them)
       exclusive_interests = set();
       interest_counts = {};
       
       for customer in customers {
           for interest in customer.interests {
               interest_counts[interest] = (interest_counts[interest] or 0) + 1;
           }
       }
       
       for interest, count in interest_counts.entries() {
           if count == 1 {
               exclusive_interests.add(interest);
           }
       }
       
       return {
           "total_customers": customers.length(),
           "unique_interests": all_interests.length(),
           "unique_locations": all_locations.length(),
           "unique_age_groups": all_age_groups.length(),
           "popular_combinations": interest_combinations.entries()
               .sorted((a, b) => b[1] - a[1])
               .take(10),
           "exclusive_interests": exclusive_interests.list()
       };
   }

Performance Tips
----------------

Use Sets for Membership Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - O(1) membership test
   large_set = set(1..1000000);
   if 999999 in large_set {  # Fast
       # ...
   }
   
   # Slow - O(n) membership test
   large_list = (1..1000000).list();
   if 999999 in large_list {  # Slow
       # ...
   }

Use Set Operations Instead of Loops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - set operations are optimized
   common = set1 & set2;
   
   # Less efficient
   common = [];
   for item in set1 {
       if item in set2 {
           common.append(item);
       }
   }

Use Comprehensions for Set Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - set comprehension
   unique_squares = {x * x for x in 1..1000};
   
   # Less efficient
   unique_squares = set();
   for x in 1..1000 {
       unique_squares.add(x * x);
   }