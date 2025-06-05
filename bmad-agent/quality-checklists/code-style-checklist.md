# Code Style Consistency Checklist

## Purpose
Systematic checklist for validating coding style consistency against project-discovered patterns and ensuring new code matches established conventions before code review and deployment.

## Pre-Code Generation Style Checks

### 1. Style Memory Validation
- [ ] **Load Project Style Rules**: Query memory for coding-style entries for target language
- [ ] **Verify Pattern Confidence**: Ensure style rules have >70% confidence from bootstrap analysis
- [ ] **Check Pattern Currency**: Validate style patterns are based on recent codebase analysis (<30 days)
- [ ] **Identify Style Conflicts**: Review any conflicting patterns and their resolution strategies

**Memory Query Commands**:
```
search_memory("coding-style {language}")
search_memory("naming-conventions {language}")
search_memory("formatting {language}")
search_memory("code-organization {language}")
```

### 2. Context Analysis
- [ ] **File Location Assessment**: Determine appropriate style context (components/, services/, utils/, etc.)
- [ ] **Surrounding Code Review**: Analyze 3-5 nearby files for local pattern consistency
- [ ] **Framework-Specific Patterns**: Apply framework conventions (React, Angular, Django, Spring, etc.)
- [ ] **Team Conventions Override**: Check for explicit team style guide overrides

## Code Generation Style Application

### 3. Naming Convention Compliance

#### Variables and Functions
- [ ] **Variable Naming**: Follows discovered pattern (camelCase, snake_case, PascalCase)
- [ ] **Function Naming**: Uses established verb-noun patterns (get*, set*, handle*, process*, validate*)
- [ ] **Boolean Variables**: Follows is*, has*, can*, should* prefixes where applicable
- [ ] **Constants**: Uses project-specific constant naming (SCREAMING_SNAKE_CASE, camelCase)
- [ ] **Private Members**: Follows privacy indication pattern (underscore prefix, private keyword, readonly)

**Validation Examples**:
```typescript
// ✅ Following discovered camelCase pattern
const userName = 'john_doe';
const isUserActive = true;
const handleUserUpdate = () => {};

// ❌ Violating discovered pattern  
const user_name = 'john_doe';
const IsUserActive = true;
const HandleUserUpdate = () => {};
```

#### Classes and Interfaces
- [ ] **Class Naming**: Uses discovered pattern (PascalCase, noun-based)
- [ ] **Interface Naming**: Follows project convention (I-prefix, descriptive names, -Interface suffix)
- [ ] **Abstract Classes**: Uses established abstract class patterns
- [ ] **Generic Types**: Follows type parameter naming conventions

#### Files and Modules
- [ ] **File Naming**: Matches project pattern (kebab-case, PascalCase, snake_case)
- [ ] **Directory Structure**: Follows established organization (feature-based, type-based)
- [ ] **Index Files**: Uses consistent index.* patterns
- [ ] **Extension Conventions**: Matches project file extension patterns (.ts, .tsx, .component.ts)

### 4. Formatting Rule Compliance

#### Indentation and Spacing
- [ ] **Indentation Style**: Uses discovered pattern (2 spaces, 4 spaces, tabs)
- [ ] **Line Length**: Respects project maximum (80, 100, 120 characters)
- [ ] **Operator Spacing**: Consistent spacing around operators (a + b vs a+b)
- [ ] **Function Call Spacing**: Matches project pattern for function calls and parameters

#### Brackets and Braces
- [ ] **Brace Style**: Follows established pattern (same-line, new-line opening braces)
- [ ] **Bracket Spacing**: Consistent array and object literal formatting
- [ ] **Conditional Formatting**: Matches if/else, switch statement formatting patterns
- [ ] **Function Parameter Formatting**: Follows multi-line parameter formatting rules

#### Quotes and Semicolons
- [ ] **Quote Style**: Uses discovered preference (single quotes, double quotes)
- [ ] **Template Literals**: Appropriate usage for string interpolation
- [ ] **Semicolon Usage**: Follows project pattern (always, never, ASI)
- [ ] **Trailing Commas**: Matches project preference (always, never, multiline-only)

**Validation Examples**:
```javascript
// ✅ Following discovered single-quote, semicolon pattern
const message = 'Hello, world!';
const greeting = `Hello, ${userName}!`;

// ❌ Violating discovered pattern
const message = "Hello, world!"
const greeting = "Hello, " + userName + "!"
```

### 5. Code Organization Compliance

#### Import/Include Organization
- [ ] **Import Grouping**: Follows discovered pattern (external, internal, relative)
- [ ] **Import Sorting**: Uses established sorting (alphabetical, type-based, length)
- [ ] **Import Spacing**: Consistent empty lines between import groups
- [ ] **Alias Patterns**: Uses consistent import aliasing conventions

**Validation Examples**:
```typescript
// ✅ Following discovered import organization
import React from 'react';
import axios from 'axios';

import { UserService } from '../services/user.service';
import { ValidationUtils } from '../utils/validation';

import './Component.styles.css';
import { ChildComponent } from './ChildComponent';
```

#### Function and Class Organization
- [ ] **Method Ordering**: Follows discovered pattern (constructor, public, private, static)
- [ ] **Function Length**: Respects established function length preferences
- [ ] **Class Member Organization**: Uses consistent property, method, static ordering
- [ ] **Comment Placement**: Follows project documentation patterns

### 6. Language-Specific Pattern Compliance

#### JavaScript/TypeScript
- [ ] **Type Annotations**: Consistent usage of explicit vs inferred types
- [ ] **Arrow Functions**: Follows project preference for arrow vs function declarations
- [ ] **Async/Await**: Uses established async pattern preferences
- [ ] **Destructuring**: Consistent destructuring usage patterns
- [ ] **Optional Chaining**: Appropriate usage of ?. and ?? operators

#### Python
- [ ] **Import Style**: Follows PEP 8 and project-specific import patterns
- [ ] **Function Definitions**: Uses consistent function and method definition style
- [ ] **List Comprehensions**: Follows project preference for comprehensions vs loops
- [ ] **Class Method Organization**: Uses established method ordering patterns

#### Java
- [ ] **Access Modifiers**: Explicit vs implicit public/private usage
- [ ] **Generic Usage**: Consistent generic type parameter patterns
- [ ] **Exception Handling**: Follows established exception handling patterns
- [ ] **Annotation Placement**: Consistent annotation usage and placement

## Post-Code Generation Validation

### 7. Consistency Score Assessment
- [ ] **Calculate Consistency Score**: Compare generated code against project patterns
- [ ] **Target Score Verification**: Ensure >95% consistency with established patterns
- [ ] **Pattern Deviation Documentation**: Document any intentional pattern deviations
- [ ] **Context-Specific Validation**: Verify patterns appropriate for code context

### 8. Cross-File Consistency Check
- [ ] **Related File Analysis**: Compare with similar components/modules in project
- [ ] **API Consistency**: Ensure consistent naming with related API endpoints
- [ ] **State Management Patterns**: Follow established state/data flow patterns
- [ ] **Error Handling Consistency**: Use project-standard error handling approaches

### 9. Tool Configuration Compliance
- [ ] **Linter Configuration**: Code passes project linter rules without violations
- [ ] **Formatter Compatibility**: Code aligns with project formatter configuration
- [ ] **Pre-commit Hooks**: Code passes all style-related pre-commit checks
- [ ] **IDE Integration**: Code formatting matches project IDE settings

## Quality Gate Integration

### 10. Style Quality Gates

#### Pre-Commit Gate
- [ ] **Zero Style Violations**: No linting errors or warnings
- [ ] **Consistency Score**: >95% consistency with project patterns
- [ ] **Pattern Compliance**: All major style categories pass validation
- [ ] **Tool Integration**: Automated tools pass without manual intervention

#### Code Review Gate
- [ ] **Reviewer Style Check**: Manual verification of style consistency
- [ ] **Pattern Appropriateness**: Style choices appropriate for context
- [ ] **Documentation Quality**: Comments and documentation follow project standards
- [ ] **Future Maintainability**: Style choices support long-term maintainability

#### Deployment Gate
- [ ] **Production Readiness**: Style meets production code standards
- [ ] **Performance Impact**: Style choices don't negatively impact performance
- [ ] **Security Compliance**: Style patterns don't introduce security vulnerabilities
- [ ] **Monitoring Compatibility**: Code style supports monitoring and debugging

## Automated Validation Integration

### 11. Memory-Enhanced Validation
```python
def validate_style_consistency(generated_code, language, context):
    """Automated style consistency validation"""
    
    # Load project patterns
    style_rules = load_style_rules_from_memory(language)
    
    # Analyze generated code
    consistency_score = calculate_consistency_score(generated_code, style_rules)
    violations = detect_style_violations(generated_code, style_rules)
    
    # Generate validation report
    return {
        "consistency_score": consistency_score,
        "violations": violations,
        "passing": consistency_score > 0.95 and len(violations) == 0,
        "recommendations": generate_style_recommendations(violations)
    }
```

### 12. Continuous Style Learning
- [ ] **Pattern Reinforcement**: Successfully validated patterns increase confidence
- [ ] **Exception Documentation**: Style deviations are documented with context
- [ ] **Team Feedback Integration**: Code review feedback updates style patterns
- [ ] **Evolution Tracking**: Style pattern changes are tracked over time

## Style Emergency Procedures

### 13. Style Conflict Resolution
- [ ] **Pattern Conflict Identification**: Detect when multiple valid patterns exist
- [ ] **Context-Based Resolution**: Choose pattern based on immediate code context
- [ ] **Team Consultation**: Escalate significant style decisions to team
- [ ] **Documentation Update**: Document resolution for future reference

### 14. Legacy Code Integration
- [ ] **Legacy Pattern Analysis**: Understand existing patterns in legacy sections
- [ ] **Gradual Migration Strategy**: Plan for gradual style standardization
- [ ] **Compatibility Maintenance**: Ensure new code doesn't break legacy integration
- [ ] **Refactoring Opportunities**: Identify opportunities for style improvement

## Checklist Usage Examples

### Example 1: React Component Style Validation
```markdown
## Style Checklist: UserProfileComponent.tsx

### Pre-Generation Checks
✅ Loaded TypeScript React style rules from memory (confidence: 94%)
✅ Analyzed surrounding components in /components/user/
✅ Identified React functional component pattern
✅ Found established prop interface pattern (I*Props)

### Generated Code Validation
✅ Component naming: UserProfileComponent (follows PascalCase + Component suffix)
✅ Props interface: IUserProfileProps (follows I-prefix pattern)
✅ Hook usage: useState<UserData | null> (follows explicit typing pattern)
✅ Event handlers: handleUserUpdate (follows handle* prefix pattern)
✅ Import organization: React imports first, then internal modules
✅ Formatting: 2-space indent, single quotes, trailing commas

### Style Score: 98% ✅
### Violations: 0 ✅
### Ready for Code Review: ✅
```

### Example 2: Python Service Style Validation
```markdown
## Style Checklist: user_service.py

### Pre-Generation Checks
✅ Loaded Python Django style rules from memory (confidence: 91%)
✅ Analyzed existing services in /services/
✅ Identified snake_case naming pattern
✅ Found established class-based service pattern

### Generated Code Validation
✅ Class naming: UserService (follows PascalCase service pattern)
✅ Method naming: get_user_by_id (follows snake_case verb_noun pattern)
✅ Import organization: Django imports, third-party, then local
✅ Exception handling: Specific exceptions with messages
✅ Docstrings: Google-style docstrings for public methods
✅ Type hints: Consistent usage throughout

### Style Score: 96% ✅
### Violations: 0 ✅
### Ready for Code Review: ✅
```

This checklist ensures that all generated code maintains high consistency with established project patterns while providing clear validation criteria and automated checking capabilities.