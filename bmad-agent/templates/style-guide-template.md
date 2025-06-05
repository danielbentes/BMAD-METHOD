# {Project Name} Code Style Guide

**Generated from codebase analysis**  
**Analysis Date**: {analysis_date}  
**Files Analyzed**: {total_files} across {language_count} languages  
**Overall Confidence**: {average_confidence}%

---

## Quick Reference

### Primary Languages
| Language | Files | Confidence | Status |
|----------|-------|------------|--------|
| {language_1} | {file_count} | {confidence}% | {status} |
| {language_2} | {file_count} | {confidence}% | {status} |
| {language_3} | {file_count} | {confidence}% | {status} |

### Key Patterns
- **Naming**: {primary_naming_pattern}
- **Formatting**: {primary_formatting_pattern}
- **Organization**: {primary_organization_pattern}

---

## {Primary Language} Style Rules

### Naming Conventions

#### Variables
**Pattern**: {variable_pattern} (Confidence: {confidence}%)

```{language}
// ✅ Correct
const userName = 'john';
const isUserActive = true;
const userProfileData = {};

// ❌ Incorrect
const user_name = 'john';
const IsUserActive = true;
const UserProfileData = {};
```

**Common Patterns**:
- Boolean variables: `is*`, `has*`, `can*`, `should*`
- Collections: `*List`, `*Array`, `*Set` (plural nouns)
- Constants: `{constant_pattern}`

#### Functions/Methods
**Pattern**: {function_pattern} (Confidence: {confidence}%)

```{language}
// ✅ Correct
function getUserData() {}
function validateUserInput() {}
function handleUserSubmission() {}

// ❌ Incorrect
function get_user_data() {}
function ValidateUserInput() {}
function HandleUserSubmission() {}
```

**Verb Patterns**:
- Data retrieval: `get*`, `fetch*`, `load*`
- Data modification: `set*`, `update*`, `modify*`
- Validation: `validate*`, `check*`, `verify*`
- Event handling: `handle*`, `on*`, `process*`
- Utilities: `format*`, `parse*`, `convert*`

#### Classes/Interfaces
**Pattern**: {class_pattern} (Confidence: {confidence}%)

```{language}
// ✅ Correct
class UserManager {}
interface UserRepository {}
abstract class BaseValidator {}

// ❌ Incorrect
class userManager {}
interface userRepository {}
abstract class baseValidator {}
```

**Interface Patterns**:
- Interfaces: {interface_pattern}
- Abstract classes: {abstract_pattern}
- Implementation classes: {implementation_pattern}

#### Files/Modules
**Pattern**: {file_pattern} (Confidence: {confidence}%)

```
// ✅ Correct Directory Structure
src/
  components/
    user-profile.component.ts
    user-list.component.ts
  services/
    user.service.ts
    auth.service.ts
  utils/
    string-helpers.ts
    date-formatters.ts

// ❌ Incorrect
src/
  Components/
    UserProfile.ts
    userList.component.ts
  Services/
    User_Service.ts
```

### Formatting Rules

#### Indentation
**Rule**: {indentation_rule} (Confidence: {confidence}%)

```{language}
// ✅ Correct
function processData(data) {
{indent_example}if (data.isValid) {
{indent_example}{indent_example}return processValidData(data);
{indent_example}}
{indent_example}return handleInvalidData(data);
}

// ❌ Incorrect
function processData(data) {
{wrong_indent_example}if (data.isValid) {
{wrong_indent_example}return processValidData(data);
{wrong_indent_example}}
{wrong_indent_example}return handleInvalidData(data);
}
```

#### Line Length
**Rule**: Maximum {max_line_length} characters (Confidence: {confidence}%)

```{language}
// ✅ Correct - Proper line breaking
const result = await processUserDataWithValidation(
  userData,
  validationRules,
  {
    strict: true,
    throwOnError: false
  }
);

// ❌ Incorrect - Line too long
const result = await processUserDataWithValidation(userData, validationRules, { strict: true, throwOnError: false });
```

#### Quotes and Semicolons
**Quotes**: {quote_rule} (Confidence: {confidence}%)  
**Semicolons**: {semicolon_rule} (Confidence: {confidence}%)

```{language}
// ✅ Correct
const message = {quote_example}'Hello, world!'{quote_example}{semicolon_example}
const template = {template_quote_example}`User: ${userName}`{template_quote_example}{semicolon_example}

// ❌ Incorrect
const message = {wrong_quote_example}"Hello, world!"{wrong_quote_example}{wrong_semicolon_example}
```

#### Brackets and Braces
**Style**: {bracket_style} (Confidence: {confidence}%)

```{language}
// ✅ Correct
if (condition) {
  doSomething();
} else {
  doSomethingElse();
}

const obj = {
  property1: 'value1',
  property2: 'value2'
};

// ❌ Incorrect (if different style detected)
if (condition)
{
  doSomething();
}
else
{
  doSomethingElse();
}
```

#### Spacing
**Rules**: (Confidence: {confidence}%)

```{language}
// ✅ Correct spacing
const result = a + b * c;
if (x === y) {}
function myFunc(param1, param2) {}
const array = [1, 2, 3];
const object = { key: 'value' };

// ❌ Incorrect spacing
const result = a+b*c;
if(x===y){}
function myFunc(param1,param2){}
const array = [1,2,3];
const object = {key:'value'};
```

### Code Organization

#### Import/Include Order
**Pattern**: {import_pattern} (Confidence: {confidence}%)

```{language}
// ✅ Correct import order
// 1. Built-in/standard library imports
import fs from 'fs';
import path from 'path';

// 2. Third-party library imports
import React from 'react';
import axios from 'axios';
import lodash from 'lodash';

// 3. Internal application imports
import { UserService } from '../services/user.service';
import { ValidationUtils } from '../utils/validation';

// 4. Relative imports
import './component.styles.css';
import { ChildComponent } from './child-component';
```

#### Function Organization
**Pattern**: {function_organization} (Confidence: {confidence}%)

```{language}
class UserManager {
  // 1. Static properties
  static readonly DEFAULT_ROLE = 'user';
  
  // 2. Instance properties
  private readonly userRepository: UserRepository;
  
  // 3. Constructor
  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository;
  }
  
  // 4. Public methods
  public async createUser(userData: UserData): Promise<User> {
    // Implementation
  }
  
  public async updateUser(id: string, updates: Partial<UserData>): Promise<User> {
    // Implementation
  }
  
  // 5. Private methods
  private validateUserData(userData: UserData): boolean {
    // Implementation
  }
  
  // 6. Static methods
  static isValidRole(role: string): boolean {
    // Implementation
  }
}
```

#### File Structure
**Pattern**: {file_structure_pattern}

```
// ✅ Recommended file organization
src/
  {component_directory}/           # {organization_explanation}
    {example_component_1}/
      {file_1}.{ext}
      {file_2}.{ext}
      index.{ext}
    {example_component_2}/
      {file_1}.{ext}
      {file_2}.{ext}
  {service_directory}/
    {example_service}.{ext}
  {utility_directory}/
    {example_utility}.{ext}
```

### Comments and Documentation

#### Comment Style
**Pattern**: {comment_pattern} (Confidence: {confidence}%)

```{language}
// ✅ Correct comment style

/**
 * Processes user authentication with JWT tokens
 * @param credentials - User login credentials
 * @param options - Authentication options
 * @returns Promise resolving to authentication result
 */
async function authenticateUser(
  credentials: LoginCredentials,
  options: AuthOptions = {}
): Promise<AuthResult> {
  // Validate input parameters
  if (!credentials.email || !credentials.password) {
    throw new ValidationError('Email and password are required');
  }
  
  // Process authentication logic
  const result = await this.authService.validate(credentials);
  
  return result;
}

// Inline comments for complex logic
const complexCalculation = (
  // Apply business rule: 15% discount for premium users
  basePrice * (user.isPremium ? 0.85 : 1.0)
) * taxRate;
```

#### Documentation Requirements
**Level**: {documentation_level}

- **Public APIs**: {public_api_requirement}
- **Complex functions**: {complex_function_requirement}
- **Business logic**: {business_logic_requirement}
- **Error conditions**: {error_documentation_requirement}

---

## {Secondary Language} Style Rules

### Naming Conventions
{secondary_language_naming_rules}

### Formatting Rules
{secondary_language_formatting_rules}

### Code Organization
{secondary_language_organization_rules}

---

## Enforcement Tools

### Linting Configuration
**Primary Tool**: {primary_linter}  
**Config File**: `{linter_config_path}`  
**Status**: {linter_status}

```json
// Example configuration excerpt
{
  "{setting_1}": "{value_1}",
  "{setting_2}": "{value_2}",
  "{setting_3}": "{value_3}"
}
```

### Formatting Configuration
**Primary Tool**: {primary_formatter}  
**Config File**: `{formatter_config_path}`  
**Status**: {formatter_status}

### Pre-commit Hooks
**Status**: {precommit_status}  
**Checks Enabled**:
- [ ] {check_1}
- [ ] {check_2}
- [ ] {check_3}

### IDE Configuration
**Recommended Settings**:
```json
{
  "editor.tabSize": {tab_size},
  "editor.insertSpaces": {use_spaces},
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "{action_1}": true,
    "{action_2}": true
  }
}
```

---

## Style Exceptions and Notes

### Documented Exceptions
These patterns have lower confidence or conflicting usage:

#### {Exception Category 1}
**Issue**: {exception_description}  
**Files Affected**: {affected_file_count}  
**Recommendation**: {resolution_recommendation}

```{language}
// Found Pattern A ({confidence_a}% of files)
{pattern_a_example}

// Found Pattern B ({confidence_b}% of files)
{pattern_b_example}

// Recommended: {recommended_pattern}
{recommended_example}
```

#### {Exception Category 2}
**Issue**: {exception_description}  
**Context**: {context_explanation}  
**Resolution**: {resolution_approach}

### Legacy Code Patterns
Some older files use different conventions:
- {legacy_pattern_1}: Found in {file_count} files from {time_period}
- {legacy_pattern_2}: Found in {file_count} files from {time_period}

**Migration Strategy**: {migration_approach}

---

## Style Guide Maintenance

### Confidence Scores
| Category | Confidence | Status | Action Needed |
|----------|------------|--------|---------------|
| Naming Conventions | {naming_confidence}% | {naming_status} | {naming_action} |
| Formatting Rules | {formatting_confidence}% | {formatting_status} | {formatting_action} |
| Code Organization | {organization_confidence}% | {organization_status} | {organization_action} |

### Review Schedule
- **Last Analysis**: {last_analysis_date}
- **Next Review**: {next_review_date}
- **Trigger Conditions**: 
  - {review_trigger_1}
  - {review_trigger_2}
  - {review_trigger_3}

### Contributing to Style Guide
1. **For New Patterns**: Document with examples and rationale
2. **For Changes**: Update with team consensus and migration plan
3. **For Exceptions**: Justify with specific context and scope

---

## Implementation Checklist

### For New Code
- [ ] Run style analysis: `/style-check {language}`
- [ ] Apply naming conventions from this guide
- [ ] Format code according to project rules
- [ ] Organize imports/includes per project pattern
- [ ] Add appropriate comments and documentation

### For Code Reviews
- [ ] Verify style consistency with project patterns
- [ ] Check for anti-patterns and violations
- [ ] Validate documentation completeness
- [ ] Ensure tool configuration compliance

### For Refactoring
- [ ] Update code to match current style standards
- [ ] Run automated formatting tools
- [ ] Update related documentation
- [ ] Test style changes don't break functionality

---

*This style guide was automatically generated from project analysis. For questions or suggestions, refer to the project's contribution guidelines.*

**Memory Integration**: Style rules are stored in project memory for automatic application during code generation. Query with: `search_memory("coding-style {language}")`