# Common Coding Style Patterns

## Overview
This document catalogs widely-adopted coding style patterns across different programming languages to serve as defaults when project-specific patterns cannot be determined with sufficient confidence.

## Universal Style Principles

### 1. Consistency Over Preference
- Follow established patterns within the codebase
- When in doubt, match the surrounding code
- Document intentional deviations

### 2. Readability First
- Optimize for human readers, not just compilers
- Use descriptive names over clever abbreviations
- Maintain consistent formatting

### 3. Maintainability Focus
- Write code that's easy to modify
- Use patterns that scale with project growth
- Minimize cognitive load for future developers

## Language-Specific Common Patterns

### JavaScript/TypeScript

#### Naming Conventions
```javascript
// Variables and functions: camelCase
const userName = 'john';
const userProfileData = {};

function getUserData() {}
function validateUserInput() {}

// Constants: SCREAMING_SNAKE_CASE or camelCase
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';

// Classes and interfaces: PascalCase
class UserManager {}
interface UserRepository {}

// Files: kebab-case
// user-service.ts, user-profile.component.ts

// Private members: underscore prefix (optional)
class UserService {
  private _internalState = {};
  private _validateInput() {}
}
```

#### Formatting Patterns
```javascript
// Indentation: 2 spaces (most common)
function processData(data) {
  if (data.isValid) {
    return processValidData(data);
  }
  return handleInvalidData(data);
}

// Quotes: Single quotes for strings, template literals for interpolation
const message = 'Hello, world!';
const greeting = `Hello, ${userName}!`;

// Semicolons: Always use (safer option)
const result = calculateValue();
const data = fetchData();

// Object formatting: Trailing commas in multiline
const config = {
  apiUrl: 'https://api.example.com',
  timeout: 5000,
  retries: 3, // trailing comma
};
```

#### Code Organization
```javascript
// Import order: External, internal, relative
import React from 'react';
import axios from 'axios';

import { UserService } from '../services';
import { validateInput } from '../utils';

import './Component.css';
import { ChildComponent } from './ChildComponent';
```

### Python

#### Naming Conventions
```python
# Variables and functions: snake_case
user_name = 'john'
user_profile_data = {}

def get_user_data():
    pass

def validate_user_input():
    pass

# Constants: SCREAMING_SNAKE_CASE
MAX_RETRY_ATTEMPTS = 3
API_BASE_URL = 'https://api.example.com'

# Classes: PascalCase
class UserManager:
    pass

class UserRepository:
    pass

# Files: snake_case
# user_service.py, user_profile_manager.py

# Private members: single underscore prefix
class UserService:
    def __init__(self):
        self._internal_state = {}
    
    def _validate_input(self):
        pass
```

#### Formatting Patterns
```python
# Indentation: 4 spaces (PEP 8 standard)
def process_data(data):
    if data.is_valid:
        return process_valid_data(data)
    return handle_invalid_data(data)

# Line length: 79-88 characters (PEP 8: 79, modern: 88)
def long_function_name_with_many_parameters(
    parameter_one,
    parameter_two,
    parameter_three
):
    pass

# Quotes: Single or double (be consistent)
message = 'Hello, world!'
# or
message = "Hello, world!"

# String formatting: f-strings (Python 3.6+)
greeting = f'Hello, {user_name}!'
```

### Java

#### Naming Conventions
```java
// Variables and methods: camelCase
String userName = "john";
Map<String, Object> userProfileData = new HashMap<>();

public void getUserData() {}
public void validateUserInput() {}

// Constants: SCREAMING_SNAKE_CASE
public static final int MAX_RETRY_ATTEMPTS = 3;
public static final String API_BASE_URL = "https://api.example.com";

// Classes and interfaces: PascalCase
public class UserManager {}
public interface UserRepository {}

// Packages: lowercase with dots
package com.company.userservice;

// Files: Match class name (PascalCase)
// UserService.java, UserProfileManager.java
```

#### Formatting Patterns
```java
// Indentation: 4 spaces or 1 tab
public void processData(UserData data) {
    if (data.isValid()) {
        return processValidData(data);
    }
    return handleInvalidData(data);
}

// Braces: Same line (most common in Java)
if (condition) {
    doSomething();
} else {
    doSomethingElse();
}

// Line length: 120 characters (modern standard)
public UserProfile createUserProfile(
    String userName,
    String email,
    Map<String, Object> preferences
) {
    // Implementation
}
```

### C#

#### Naming Conventions
```csharp
// Variables and methods: camelCase for local, PascalCase for public
string userName = "john";
private Dictionary<string, object> userProfileData;

public void GetUserData() {}
public void ValidateUserInput() {}

// Constants: PascalCase
public const int MaxRetryAttempts = 3;
public const string ApiBaseUrl = "https://api.example.com";

// Classes and interfaces: PascalCase
public class UserManager {}
public interface IUserRepository {}

// Namespaces: PascalCase
namespace Company.UserService {}

// Files: Match class name (PascalCase)
// UserService.cs, UserProfileManager.cs
```

## Cross-Language Universal Patterns

### Function/Method Organization
```
1. Constructor/initialization
2. Public methods (alphabetical or logical grouping)
3. Protected methods
4. Private methods
5. Static methods
6. Properties/getters/setters (language dependent)
```

### Comment Patterns
```javascript
/**
 * Main documentation comment
 * @param {Type} param - Parameter description
 * @returns {Type} Return value description
 */
function documentedFunction(param) {
    // Inline comment explaining complex logic
    const result = complexCalculation(param);
    
    /* Block comment for
       multi-line explanations
       of complex sections */
    return result;
}
```

### Error Handling Patterns
```javascript
// Explicit error handling
try {
    const result = await riskyOperation();
    return result;
} catch (error) {
    logger.error('Operation failed', { error, context });
    throw new ServiceError('Operation failed', error);
}

// Guard clauses
function processUser(user) {
    if (!user) {
        throw new Error('User is required');
    }
    
    if (!user.id) {
        throw new Error('User ID is required');
    }
    
    // Main logic here
    return processValidUser(user);
}
```

## Industry-Standard Tool Configurations

### ESLint (JavaScript/TypeScript)
```json
{
  "extends": ["@typescript-eslint/recommended"],
  "rules": {
    "indent": ["error", 2],
    "quotes": ["error", "single"],
    "semi": ["error", "always"],
    "no-console": "warn",
    "no-debugger": "error"
  }
}
```

### Prettier (JavaScript/TypeScript)
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

### Black (Python)
```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
```

### rustfmt (Rust)
```toml
edition = "2021"
max_width = 100
hard_tabs = false
tab_spaces = 4
```

## Framework-Specific Patterns

### React/JSX
```jsx
// Component naming: PascalCase
export const UserProfile = ({ user, onUpdate }) => {
    // Hooks first
    const [isEditing, setIsEditing] = useState(false);
    const [formData, setFormData] = useState(user);
    
    // Event handlers: handle* prefix
    const handleSubmit = (event) => {
        event.preventDefault();
        onUpdate(formData);
    };
    
    const handleCancel = () => {
        setIsEditing(false);
        setFormData(user);
    };
    
    // Early returns for conditions
    if (!user) {
        return <div>Loading...</div>;
    }
    
    // Main render
    return (
        <div className="user-profile">
            {/* Component JSX */}
        </div>
    );
};
```

### Express.js (Node.js)
```javascript
// Route handlers: verb + noun pattern
app.get('/api/users', getUserList);
app.post('/api/users', createUser);
app.put('/api/users/:id', updateUser);
app.delete('/api/users/:id', deleteUser);

// Middleware naming: verb + middleware
const authenticateUser = (req, res, next) => {
    // Authentication logic
    next();
};

const validateUserInput = (req, res, next) => {
    // Validation logic
    next();
};
```

### Django (Python)
```python
# Model naming: singular PascalCase
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

# View naming: verb + noun
def list_users(request):
    pass

def create_user(request):
    pass

# URL patterns: lowercase with hyphens
urlpatterns = [
    path('users/', list_users, name='user-list'),
    path('users/create/', create_user, name='user-create'),
]
```

## Configuration File Patterns

### Package Manager Files
```json
// package.json, composer.json
{
  "name": "project-name",
  "version": "1.0.0",
  "description": "Project description",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "jest",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  }
}
```

### Environment Configuration
```bash
# .env files: SCREAMING_SNAKE_CASE
DATABASE_URL=postgresql://localhost/myapp
API_KEY=your-api-key-here
DEBUG=true
PORT=3000

# Boolean values: true/false (lowercase)
ENABLE_LOGGING=true
USE_CACHE=false
```

## Anti-Patterns to Avoid

### Universal Anti-Patterns
```javascript
// ❌ Inconsistent naming
const userName = 'john';
const user_email = 'john@example.com';
const UserAge = 25;

// ❌ Magic numbers/strings
if (status === 200) {} // What does 200 mean?
setTimeout(callback, 30000); // Why 30000?

// ❌ Unclear abbreviations
const usr = getUsr(); // What is usr?
const calc = performCalc(); // What kind of calculation?

// ❌ Deep nesting
if (user) {
    if (user.profile) {
        if (user.profile.settings) {
            if (user.profile.settings.notifications) {
                // Too deep!
            }
        }
    }
}

// ✅ Better with guard clauses
if (!user?.profile?.settings?.notifications) {
    return;
}
// Handle notifications
```

### Language-Specific Anti-Patterns

#### JavaScript/TypeScript
```javascript
// ❌ Using var instead of const/let
var userName = 'john'; // Use const or let

// ❌ Not using semicolons consistently
const a = 1
const b = 2; // Inconsistent

// ❌ Mixed quote styles
const message1 = 'Hello';
const message2 = "World"; // Inconsistent
```

#### Python
```python
# ❌ Mixing spaces and tabs
def bad_function():
    if True:
        return "mixed indentation"  # 4 spaces
	    return "this is bad"        # tab

# ❌ Not following PEP 8 naming
def GetUserData():  # Should be get_user_data()
    pass

class userManager:  # Should be UserManager
    pass
```

## Style Pattern Confidence Scoring

### High Confidence Patterns (90%+)
Use these patterns when no project-specific style is detected:
- **Naming**: Follow language conventions (camelCase for JS, snake_case for Python)
- **Indentation**: 2 spaces for JS/TS, 4 spaces for Python/Java
- **Line Length**: 80-100 characters depending on language
- **File Organization**: Imports at top, exports at bottom

### Medium Confidence Patterns (70-89%)
Consider these when multiple valid options exist:
- **Quote Style**: Single quotes for JS (unless templates needed)
- **Semicolon Usage**: Always use in JS/TS for safety
- **Bracket Style**: Same line for opening braces in most languages

### Project-Specific Decisions (Context Dependent)
These should always be detected from the project:
- **Import Organization**: Varies significantly between projects
- **Comment Density**: Depends on team preferences and domain complexity
- **Function Length**: Varies by architecture and complexity
- **Error Handling Strategy**: Project and team dependent

This pattern library serves as a fallback when project-specific analysis doesn't yield confident results, ensuring consistent code generation even in ambiguous situations.