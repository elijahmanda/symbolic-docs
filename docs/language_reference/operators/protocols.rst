Protocols
=========

Protocols in Symbolic define interfaces that types can implement, enabling structural typing and polymorphism.

Defining Protocols
------------------

Basic Protocol Definition
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Drawable {
       fn draw(self, surface);
       fn get_bounds(self) -> Rectangle;
   }

   protocol Serializable {
       fn serialize(self) -> String;
       fn deserialize(cls, data: String) -> Self;
   }

   protocol Comparable {
       fn compare(self, other: Self) -> Ordering;
   }

Protocol with Default Implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Collection {
       fn is_empty(self) -> Boolean;
       fn length(self) -> Integer;
       
       # Default implementation
       fn is_not_empty(self) -> Boolean {
           return !self.is_empty();
       }
   }

   protocol Iterable {
       fn __iter__(self);
       
       # Default implementations
       fn map(self, transform) {
           result = [];
           for item in self {
               result.append(transform(item));
           }
           return result;
       }
       
       fn filter(self, predicate) {
           result = [];
           for item in self {
               if predicate(item) {
                   result.append(item);
               }
           }
           return result;
       }
   }

Implementing Protocols
----------------------

Explicit Implementation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   class Circle implements Drawable {
       center: Point;
       radius: Float;
       
       fn draw(self, surface) {
           # Drawing implementation for circle
           surface.draw_circle(self.center, self.radius);
       }
       
       fn get_bounds(self) -> Rectangle {
           return Rectangle(
               self.center.x - self.radius,
               self.center.y - self.radius,
               self.radius * 2,
               self.radius * 2
           );
       }
   }

   class Rectangle implements Drawable, Comparable {
       x: Float, y: Float, width: Float, height: Float;
       
       fn draw(self, surface) {
           surface.draw_rectangle(self.x, self.y, self.width, self.height);
       }
       
       fn get_bounds(self) -> Rectangle {
           return self;  # Rectangle is its own bounds
       }
       
       fn compare(self, other: Rectangle) -> Ordering {
           area_self = self.width * self.height;
           area_other = other.width * other.height;
           
           if area_self < area_other {
               return Ordering.LESS;
           } else if area_self > area_other {
               return Ordering.GREATER;
           } else {
               return Ordering.EQUAL;
           }
       }
   }

Structural Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Any type with draw and get_bounds methods automatically implements Drawable
   class CustomShape {
       vertices: [Point];
       
       fn draw(self, surface) {
           surface.draw_polygon(self.vertices);
       }
       
       fn get_bounds(self) -> Rectangle {
           # Calculate bounding box from vertices
           xs = self.vertices.map(v => v.x);
           ys = self.vertices.map(v => v.y);
           return Rectangle(xs.min(), ys.min(), xs.max() - xs.min(), ys.max() - ys.min());
       }
   }

   # CustomShape automatically satisfies Drawable protocol

Protocol Composition
--------------------

Combining Protocols
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Renderable = Drawable & Serializable & Comparable;
   
   protocol CollectionWithSize = Collection & {
       fn capacity(self) -> Integer;
       fn is_full(self) -> Boolean;
   }

   class Sprite implements Renderable {
       # Must implement all methods from Drawable, Serializable, and Comparable
       fn draw(self, surface) { ... }
       fn get_bounds(self) -> Rectangle { ... }
       fn serialize(self) -> String { ... }
       fn deserialize(cls, data) -> Sprite { ... }
       fn compare(self, other) -> Ordering { ... }
   }

Generic Protocols
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Container[T] {
       fn add(self, item: T);
       fn remove(self, item: T) -> Boolean;
       fn contains(self, item: T) -> Boolean;
   }

   protocol Sequence[T] {
       fn __getitem__(self, index: Integer) -> T;
       fn __setitem__(self, index: Integer, value: T);
       fn __len__(self) -> Integer;
   }

Practical Examples
------------------

Data Storage Protocols
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol DataStore {
       fn get(self, key: String) -> Any;
       fn set(self, key: String, value: Any);
       fn delete(self, key: String) -> Boolean;
       fn keys(self) -> [String];
   }

   class MemoryStore implements DataStore {
       data: Dict = {};
       
       fn get(self, key) {
           return self.data.get(key);
       }
       
       fn set(self, key, value) {
           self.data[key] = value;
       }
       
       fn delete(self, key) {
           if key in self.data {
               del self.data[key];
               return true;
           }
           return false;
       }
       
       fn keys(self) {
           return self.data.keys().list();
       }
   }

   class FileStore implements DataStore {
       base_path: String;
       
       fn get(self, key) {
           path = self._get_path(key);
           if file.exists(path) {
               return file.read(path);
           }
           return null;
       }
       
       fn set(self, key, value) {
           path = self._get_path(key);
           file.write(path, value);
       }
       
       fn _get_path(self, key) {
           return self.base_path + "/" + key;
       }
   }

Mathematical Protocols
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol VectorSpace[V] {
       fn zero() -> V;
       fn add(self: V, other: V) -> V;
       fn scale(self: V, scalar: Float) -> V;
       fn dot(self: V, other: V) -> Float;
   }

   protocol MetricSpace[T] {
       fn distance(self: T, other: T) -> Float;
   }

   class Point2D implements VectorSpace[Point2D], MetricSpace[Point2D] {
       x: Float, y: Float;
       
       fn zero() -> Point2D {
           return Point2D(0, 0);
       }
       
       fn add(self, other: Point2D) -> Point2D {
           return Point2D(self.x + other.x, self.y + other.y);
       }
       
       fn scale(self, scalar: Float) -> Point2D {
           return Point2D(self.x * scalar, self.y * scalar);
       }
       
       fn dot(self, other: Point2D) -> Float {
           return self.x * other.x + self.y * other.y;
       }
       
       fn distance(self, other: Point2D) -> Float {
           dx = self.x - other.x;
           dy = self.y - other.y;
           return (dx^2 + dy^2).sqrt();
       }
   }

Web Framework Protocols
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Middleware {
       fn process_request(self, request) -> Request;
       fn process_response(self, request, response) -> Response;
   }

   protocol View {
       fn handle_get(self, request) -> Response;
       fn handle_post(self, request) -> Response;
       fn handle_put(self, request) -> Response;
       fn handle_delete(self, request) -> Response;
   }

   class AuthenticationMiddleware implements Middleware {
       fn process_request(self, request) -> Request {
           token = request.headers.get("Authorization");
           if token {
               user = verify_token(token);
               request.user = user;
           }
           return request;
       }
       
       fn process_response(self, request, response) -> Response {
           # Add security headers
           response.headers["X-Content-Type-Options"] = "nosniff";
           return response;
       }
   }

Protocol Checking
-----------------

Runtime Protocol Checking
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   fn requires_drawable(obj) {
       if !obj implements Drawable {
           throw "Object must implement Drawable protocol";
       }
       return obj.draw(surface);
   }

   fn create_renderer(renderable_objects) {
       for obj in renderable_objects {
           if obj implements Renderable {
               renderer.add(obj);
           } else {
               print($"Skipping object that doesn't implement Renderable: {obj}");
           }
       }
   }

Compile-time Protocol Checking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Type system ensures protocol compliance at compile time
   fn render_scene(drawables: [Drawable], surface) {
       for drawable in drawables {
           # Compiler knows drawable has draw method
           drawable.draw(surface);
       }
   }

   fn sort_comparables(comparables: [Comparable]) -> [Comparable] {
       # Compiler knows comparables can be compared
       return comparables.sorted((a, b) => a.compare(b));
   }

Advanced Patterns
-----------------

Protocol Extensions
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   extension Collection {
       fn first(self) -> Any {
           if self.is_empty() {
               return null;
           }
           return self[0];
       }
       
       fn last(self) -> Any {
           if self.is_empty() {
               return null;
           }
           return self[self.length() - 1];
       }
       
       fn join(self, separator: String = "") -> String {
           return self.map(x => x.to_string()).join(separator);
       }
   }

   # Now all Collection implementations get these methods
   numbers = [1, 2, 3];
   print(numbers.first());  # 1
   print(numbers.last());   # 3
   print(numbers.join(", "));  # "1, 2, 3"

Conditional Protocol Conformance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Addable[T] {
       fn __add__(self: T, other: T) -> T;
   }

   # Array is Addable if its elements are Addable
   impl Addable for [T] where T: Addable {
       fn __add__(self, other: [T]) -> [T] {
           return self.concat(other);
       }
   }

   # Option is Addable if its contained type is Addable
   impl Addable for Option[T] where T: Addable {
       fn __add__(self, other: Option[T]) -> Option[T] {
           match (self, other) {
               (Some(a), Some(b)) => Some(a + b);
               _ => null;
           }
       }
   }

Protocol Witnesses
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Runtime representation of protocol conformance
   drawable_witness = protocol_witness(Drawable);
   
   fn check_drawable_conformance(obj) {
       witness = drawable_witness.for_type(type(obj));
       if witness != null {
           print("Object conforms to Drawable");
           methods = witness.methods();
           print($"Available methods: {methods}");
       } else {
           print("Object does not conform to Drawable");
       }
   }

Best Practices
--------------

Protocol Design
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - focused, single responsibility
   protocol Persistable {
       fn save(self);
       fn load(cls, id) -> Self;
   }
   
   # Avoid - too broad
   protocol DoEverything {
       fn save(self);
       fn load(self);
       fn validate(self);
       fn transform(self);
       fn export(self);
   }

Use Protocols for Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good - protocol enables testing with mocks
   protocol PaymentProcessor {
       fn charge(self, amount, token) -> PaymentResult;
       fn refund(self, payment_id) -> Boolean;
   }
   
   class StripeProcessor implements PaymentProcessor {
       # Real implementation
   }
   
   class MockProcessor implements PaymentProcessor {
       # Test implementation
   }

Document Protocol Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   protocol Repository[T] {
       """
       Repository pattern for data access.
       
       Requirements:
       - find_by_id should return null if not found
       - save should create or update
       - delete should return true if deleted, false if not found
       """
       fn find_by_id(self, id) -> T;
       fn save(self, entity: T) -> T;
       fn delete(self, id) -> Boolean;
       fn find_all(self) -> [T];
   }