Imports
=======

Symbolic provides a powerful and flexible import system that supports module organization, namespacing, and dynamic loading.

Basic Imports
-------------

Simple Imports
~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Import entire module
   import math;
   result = math.sqrt(25);  # 5.0
   
   # Import with alias
   import math as mathematics;
   value = mathematics.pi;  # 3.14159
   
   # Import specific functions
   import math::{sqrt, pow};
   hypotenuse = sqrt(pow(3, 2) + pow(4, 2));  # 5.0

Selective Imports
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Import multiple items
   import std::io::{read_file, write_file, append_file};
   import math::{constants::{pi, e}, functions::{sin, cos, tan}};
   
   # Import with renaming
   import math::{sqrt as square_root, log as logarithm};
   import std::collections::{HashMap as Dict, HashSet as Set};
   
   # Wildcard import (use sparingly)
   import math::trigonometry::*;
   angle = 45 * pi / 180;
   sine_val = sin(angle);

Structured Imports
------------------

Namespace Imports
~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Deep namespace imports
   import analytics::metrics::user_engagement::{ 
       calculate_retention, 
       measure_engagement,
       track_conversion 
   };
   
   import physics::mechanics::dynamics::{
       calculate_force,
       compute_trajectory,
       analyze_collision
   } as dynamics;
   
   # Usage
   retention = calculate_retention(users);
   force = dynamics.calculate_force(mass, acceleration);

Grouped Imports
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Import related modules together
   import web::{
       http::{Request, Response, Server},
       routing::{Router, Route, Middleware},
       templating::{Template, Renderer}
   };
   
   import data::{
       storage::{Database, Cache, FileSystem},
       processing::{Transformer, Aggregator, Filter},
       serialization::{JSON, XML, CSV}
   };

Relative Imports
----------------

Package-Relative Imports
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Current package imports
   import .::utils;           # Same package
   import .::models::user;    # Submodule in same package
   import .::api::v1::routes; # Deep submodule
   
   # Parent package imports
   import ..::shared;         # Parent package
   import ..::config;         # Sibling in parent
   import ...::common;        # Grandparent package

File-Relative Imports
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Relative to current file
   import ./helpers;          # helpers.sym in same directory
   import ../utils/math;      # utils/math.sym in parent directory
   import ./models/user;      # models/user.sym in subdirectory
   
   # Complex relative paths
   import ../../shared/constants;
   import ./api/../utils/helpers;  # Can navigate up and down

Dynamic Imports
---------------

Runtime Imports
~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Conditional imports
   if use_advanced_math {
       advanced_math = import("math::advanced");
       result = advanced_math.fourier_transform(signal);
   } else {
       basic_math = import("math::basic");
       result = basic_math.fft(signal);
   }
   
   # Plugin system
   fn load_plugin(plugin_name) {
       try {
           plugin = import($"plugins::{plugin_name}");
           return plugin;
       } catch e {
           print($"Failed to load plugin {plugin_name}: {e}");
           return null;
       }
   }

Dynamic Module Loading
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Load modules based on configuration
   config = load_config();
   enabled_modules = config.get("enabled_modules", []);
   
   loaded_modules = {};
   for module_name in enabled_modules {
       try {
           module = import(module_name);
           loaded_modules[module_name] = module;
       } catch e {
           print($"Warning: Could not load module {module_name}");
       }
   }
   
   # Lazy loading
   cached_imports = {};
   fn get_module(name) {
       if name not in cached_imports {
           cached_imports[name] = import(name);
       }
       return cached_imports[name];
   }

Practical Examples
------------------

Web Application Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Main application file
   import .::config::settings;
   import .::models::{User, Post, Comment};
   import .::services::{AuthService, DatabaseService, CacheService};
   import .::api::v1::{users, posts, comments};
   import .::middleware::{auth, logging, validation};
   import .::utils::{helpers, validators, formatters};
   
   # Configure services
   db = DatabaseService(settings.database);
   auth_service = AuthService(settings.auth);
   cache = CacheService(settings.redis);
   
   # Set up API routes
   router = Router();
   router.use(logging);
   router.use(validation);
   
   router.mount("/api/v1/users", users);
   router.mount("/api/v1/posts", posts);
   router.mount("/api/v1/comments", comments);

Data Science Pipeline
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Data analysis script
   import data::acquisition::{csv_loader, api_client, database_connector};
   import data::cleaning::{handle_missing, remove_outliers, normalize};
   import data::analysis::{statistics, clustering, regression};
   import data::visualization::{plots, charts, dashboards};
   import utils::{reporting, file_io, config_loader};
   
   # Load configuration
   config = config_loader.load("analysis_config.yaml");
   
   # Data acquisition
   raw_data = csv_loader.load(config.data_file);
   api_data = api_client.fetch(config.api_endpoint);
   
   # Data processing pipeline
   clean_data = raw_data
       |> handle_missing(config.missing_strategy)
       |> remove_outliers(config.outlier_threshold)
       |> normalize(config.normalization_method);
   
   # Analysis
   stats = statistics.describe(clean_data);
   clusters = clustering.kmeans(clean_data, config.n_clusters);
   model = regression.linear_regression(clean_data, config.target);

Plugin Architecture
~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Plugin manager
   class PluginManager {
       plugins = {};
       plugin_dir = "./plugins";
       
       fn load_plugins() {
           plugin_files = list_files(self.plugin_dir, "*.sym");
           
           for file in plugin_files {
               plugin_name = file.basename().replace(".sym", "");
               try {
                   plugin = import($"../plugins/{plugin_name}");
                   
                   # Verify plugin interface
                   if plugin.has_method("initialize") and plugin.has_method("execute") {
                       plugin.initialize();
                       self.plugins[plugin_name] = plugin;
                       print($"Loaded plugin: {plugin_name}");
                   }
               } catch e {
                   print($"Failed to load plugin {plugin_name}: {e}");
               }
           }
       }
       
       fn execute_plugin(name, data) {
           if name in self.plugins {
               return self.plugins[name].execute(data);
           }
           throw $"Plugin {name} not found";
       }
   }

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Environment-specific configuration
   import shared::constants;
   import shared::utils::{env, file_system};
   
   fn load_config() {
       environment = env.get("NODE_ENV", "development");
       
       # Load base configuration
       base_config = import("./config/base");
       
       # Load environment-specific config
       try {
           env_config = import($"./config/{environment}");
           config = base_config.merge(env_config);
       } catch e {
           print($"No {environment} config found, using base config");
           config = base_config;
       }
       
       # Load local overrides if exists
       try {
           local_config = import("./config/local");
           config = config.merge(local_config);
       } catch e {
           # Local config is optional
       }
       
       return config;
   }

Advanced Import Patterns
------------------------

Circular Imports
~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Module A: models/user.sym
   import .::services::auth;  # Imported by B
   
   class User {
       fn authenticate(self, password) {
           return auth.verify_password(self, password);
       }
   }
   
   # Module B: services/auth.sym  
   import .::models::user;    # Imported by A
   
   class AuthService {
       fn verify_password(user, password) {
           # Implementation
       }
   }

Conditional Export
~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Module with conditional exports
   if env.get("FEATURE_FLAGS::NEW_MATH", false) {
       export { advanced_sqrt, advanced_log };
   } else {
       export { basic_sqrt, basic_log };
   }
   
   # Platform-specific imports
   if system.platform == "linux" {
       linux_utils = import("utils::linux");
       export linux_utils;
   } else if system.platform == "windows" {
       windows_utils = import("utils::windows");
       export windows_utils;
   }

Import Hooks
~~~~~~~~~~~~

.. code-block:: symbolic

   # Custom import behavior
   fn custom_import_hook(module_name) {
       # Check cache first
       if module_name in import_cache {
           return import_cache[module_name];
       }
       
       # Load from custom location
       custom_path = find_module_path(module_name);
       if custom_path != null {
           module = load_module_from_path(custom_path);
           import_cache[module_name] = module;
           return module;
       }
       
       # Fall back to standard import
       return import(module_name);
   }
   
   # Register hook
   set_import_hook(custom_import_hook);

Best Practices
--------------

Organize Imports Logically
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Grouped by functionality
   # Standard library
   import std::io::{read, write};
   import std::collections::{HashMap, HashSet};
   import std::math::{sqrt, pow, sin, cos};
   
   # Third-party modules
   import web::framework::{Router, Middleware};
   import data::database::{Connection, Query};
   
   # Local modules
   import .::models::{User, Post};
   import .::services::{Auth, Database};
   import .::utils::{helpers, validators};

Avoid Wildcard Imports
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Explicit imports
   import math::{sqrt, pow, sin, cos};
   
   # Avoid: Wildcard imports
   import math::*;  # Pollutes namespace

Use Aliases for Clarity
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Clear aliases
   import data::processing::analysis as data_analysis;
   import web::http::client as http_client;
   import utils::string_manipulation as str_utils;
   
   result = data_analysis.analyze_dataset(data);
   response = http_client.get(url);
   formatted = str_utils.title_case(text);

Handle Import Errors Gracefully
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: symbolic

   # Good: Error handling
   try {
       advanced_math = import("math::advanced");
   } catch e {
       print("Advanced math not available, using basic");
       advanced_math = import("math::basic");
   }
   
   # Optional imports pattern
   optional_imports = {};
   for module_name in ["fast_algorithm", "gpu_acceleration"] {
       try {
           optional_imports[module_name] = import(module_name);
       } catch e {
           # Module is optional, continue without it
       }
   }