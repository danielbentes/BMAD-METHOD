# Code Style Analysis Task

## Purpose
Systematically analyze existing codebase to extract and document coding style patterns and conventions for automatic consistency enforcement in future code generation.

## Behavioral Instructions

When user requests style analysis or during memory bootstrap:

### 1. Multi-Language Style Detection
Identify all programming languages in the project and analyze each separately:

```python
def detect_project_languages(project_root):
    """Identify languages to analyze"""
    
    language_patterns = {
        "javascript": ["*.js", "*.jsx"],
        "typescript": ["*.ts", "*.tsx"],
        "python": ["*.py"],
        "java": ["*.java"],
        "csharp": ["*.cs"],
        "go": ["*.go"],
        "rust": ["*.rs"],
        "php": ["*.php"],
        "ruby": ["*.rb"],
        "swift": ["*.swift"],
        "kotlin": ["*.kt"]
    }
    
    detected_languages = []
    for language, patterns in language_patterns.items():
        if find_files_matching_patterns(project_root, patterns):
            detected_languages.append(language)
    
    return detected_languages
```

### 2. Comprehensive Style Pattern Analysis

#### 2.1 Naming Convention Analysis
For each language, analyze:

**Variable Naming:**
- camelCase vs snake_case vs PascalCase
- Prefix/suffix patterns (is*, has*, get*, set*)
- Abbreviation usage
- Number/boolean naming patterns

**Function/Method Naming:**
- Verb patterns (process*, handle*, validate*, create*)
- Parameter naming consistency
- Return type naming influence
- Private/public method patterns

**Class/Interface Naming:**
- Noun patterns
- Interface prefixes (I*, *Interface, *Impl)
- Abstract class patterns
- Generic type naming

**File/Module Naming:**
- kebab-case vs PascalCase vs snake_case
- Index file patterns
- Feature-based vs type-based organization

#### 2.2 Code Structure Analysis

**Import/Include Organization:**
```python
def analyze_import_patterns(files):
    """Extract import organization patterns"""
    
    patterns = {
        "grouping": [],  # external, internal, relative
        "sorting": [],   # alphabetical, type-based, length
        "spacing": [],   # empty lines between groups
        "aliases": []    # common aliasing patterns
    }
    
    for file in files:
        imports = extract_imports(file)
        patterns["grouping"].append(categorize_imports(imports))
        patterns["sorting"].append(detect_sort_order(imports))
        patterns["spacing"].append(count_spacing_between_groups(imports))
        patterns["aliases"].append(extract_aliases(imports))
    
    return calculate_patterns_consensus(patterns)
```

**Function Organization:**
- Function length preferences (average, maximum)
- Parameter count patterns
- Return statement placement
- Private function placement

**Class Structure:**
- Member variable placement
- Constructor placement
- Method ordering (public first, private last, etc.)
- Static member placement

#### 2.3 Formatting Analysis

**Indentation Patterns:**
- Spaces vs tabs
- Indent size (2, 4, 8 spaces)
- Continuation line indentation
- Nested structure indentation

**Spacing and Alignment:**
- Space around operators
- Space in function calls
- Alignment of assignments
- Line spacing patterns

**Bracket and Brace Styles:**
- Same line vs new line for opening braces
- Closing brace alignment
- Array/object literal formatting
- Function parameter formatting

#### 2.4 Comment and Documentation Analysis

**Comment Patterns:**
- Inline comment frequency and style
- Block comment usage
- Documentation comment format (JSDoc, docstring, XML docs)
- Comment placement relative to code

**Documentation Standards:**
- Public API documentation requirements
- Parameter documentation patterns
- Return value documentation
- Example inclusion patterns

### 3. Pattern Confidence Scoring

```python
def calculate_pattern_confidence(pattern_instances):
    """Calculate confidence in discovered patterns"""
    
    total_instances = len(pattern_instances)
    pattern_frequency = {}
    
    # Count pattern occurrences
    for instance in pattern_instances:
        pattern = normalize_pattern(instance)
        pattern_frequency[pattern] = pattern_frequency.get(pattern, 0) + 1
    
    # Calculate confidence scores
    confidence_scores = {}
    for pattern, count in pattern_frequency.items():
        confidence = count / total_instances
        confidence_scores[pattern] = {
            "pattern": pattern,
            "confidence": confidence,
            "evidence_count": count,
            "consistency_level": determine_consistency_level(confidence)
        }
    
    return confidence_scores
```

**Confidence Levels:**
- **High (90%+)**: Pattern used consistently throughout codebase
- **Medium (70-89%)**: Pattern used frequently with few exceptions
- **Low (50-69%)**: Pattern used sometimes, inconsistent application
- **Uncertain (<50%)**: Multiple competing patterns, no clear standard

### 4. Style Rule Generation

#### 4.1 Automatic Rule Creation
```python
def generate_style_rules(analysis_results, language):
    """Generate executable style rules from analysis"""
    
    style_rules = {
        "language": language,
        "naming_conventions": {},
        "formatting_rules": {},
        "code_organization": {},
        "documentation_standards": {}
    }
    
    # Generate naming rules
    for category, patterns in analysis_results["naming"].items():
        dominant_pattern = get_highest_confidence_pattern(patterns)
        if dominant_pattern["confidence"] > 0.7:
            style_rules["naming_conventions"][category] = {
                "rule": dominant_pattern["pattern"],
                "confidence": dominant_pattern["confidence"],
                "examples": dominant_pattern["examples"][:3]
            }
    
    # Generate formatting rules
    for aspect, patterns in analysis_results["formatting"].items():
        dominant_pattern = get_highest_confidence_pattern(patterns)
        if dominant_pattern["confidence"] > 0.8:  # Higher threshold for formatting
            style_rules["formatting_rules"][aspect] = {
                "rule": dominant_pattern["pattern"],
                "confidence": dominant_pattern["confidence"]
            }
    
    return style_rules
```

#### 4.2 Exception Documentation
```python
def document_style_exceptions(analysis_results):
    """Document cases where patterns are intentionally broken"""
    
    exceptions = []
    
    for pattern_category in analysis_results:
        low_confidence_patterns = [
            p for p in pattern_category 
            if p["confidence"] < 0.7
        ]
        
        for pattern in low_confidence_patterns:
            exception = {
                "pattern_type": pattern["type"],
                "conflicting_approaches": pattern["variants"],
                "context_factors": analyze_context_factors(pattern),
                "recommendation": suggest_resolution(pattern)
            }
            exceptions.append(exception)
    
    return exceptions
```

### 5. Memory Integration

#### 5.1 Style Memory Creation
```python
def create_style_memories(style_rules, language):
    """Create memory entries for discovered style patterns"""
    
    memories = []
    
    # Naming convention memory
    if style_rules["naming_conventions"]:
        naming_memory = {
            "type": "coding-style",
            "language": language,
            "style_category": "naming-conventions",
            "rules": style_rules["naming_conventions"],
            "confidence_avg": calculate_average_confidence(
                style_rules["naming_conventions"]
            ),
            "evidence_files": extract_evidence_files(style_rules),
            "project_context": get_project_context()
        }
        memories.append(naming_memory)
    
    # Formatting memory
    if style_rules["formatting_rules"]:
        formatting_memory = {
            "type": "coding-style",
            "language": language,
            "style_category": "formatting",
            "rules": style_rules["formatting_rules"],
            "confidence_avg": calculate_average_confidence(
                style_rules["formatting_rules"]
            ),
            "enforcement_tools": detect_linter_configs(),
            "project_context": get_project_context()
        }
        memories.append(formatting_memory)
    
    # Code organization memory
    if style_rules["code_organization"]:
        organization_memory = {
            "type": "coding-style",
            "language": language,
            "style_category": "code-organization",
            "rules": style_rules["code_organization"],
            "architectural_patterns": detect_architectural_patterns(),
            "project_context": get_project_context()
        }
        memories.append(organization_memory)
    
    return memories
```

### 6. Output Formats

#### 6.1 Analysis Report Template
```markdown
# Code Style Analysis Report

## Languages Analyzed
- {language_1}: {file_count} files
- {language_2}: {file_count} files

## Style Confidence Summary
| Category | Language | Confidence | Pattern |
|----------|----------|------------|---------|
| Naming | {language} | {confidence}% | {pattern} |
| Formatting | {language} | {confidence}% | {pattern} |
| Organization | {language} | {confidence}% | {pattern} |

## Detailed Findings

### {Language} Style Patterns

#### Naming Conventions (Confidence: {confidence}%)
**Variables**: {pattern}
- Examples: `{example_1}`, `{example_2}`, `{example_3}`
- Exceptions: {exception_count} files use different pattern

**Functions**: {pattern}
- Examples: `{example_1}`, `{example_2}`, `{example_3}`
- Common prefixes: {prefix_list}

**Classes**: {pattern}
- Examples: `{example_1}`, `{example_2}`, `{example_3}`
- Interface pattern: {interface_pattern}

#### Formatting Rules (Confidence: {confidence}%)
**Indentation**: {spaces_or_tabs} ({size})
**Line Length**: {max_length} characters (average: {avg_length})
**Brackets**: {bracket_style}
**Quotes**: {quote_preference}

#### Code Organization (Confidence: {confidence}%)
**Import Order**: {import_pattern}
**Function Organization**: {function_order}
**Class Structure**: {class_organization}

## Inconsistencies Found
- {inconsistency_1}: Found in {file_count} files
- {inconsistency_2}: Found in {file_count} files

## Recommendations
1. **Enforce**: {high_confidence_patterns}
2. **Standardize**: {medium_confidence_patterns}
3. **Investigate**: {low_confidence_patterns}

## Generated Style Rules
Style rules saved to: `.bmad/project/style-guide.md`
Memory entries created: {memory_count}
```

#### 6.2 Project Style Guide Generation
```markdown
# {Project Name} Style Guide

## Overview
This style guide was generated from analysis of {file_count} files across {language_count} languages.

## {Language} Style Rules

### Naming Conventions
**Variables**: Use {pattern}
```{language}
// Good
const userName = 'john_doe';
const userProfile = {};

// Bad
const user_name = 'john_doe';
const UserProfile = {};
```

**Functions**: Use {pattern}
```{language}
// Good
function getUserData() {}
function validateUserInput() {}

// Bad
function get_user_data() {}
function ValidateUserInput() {}
```

### Formatting Rules
**Indentation**: {indent_rule}
**Line Length**: Maximum {max_length} characters
**Quotes**: Use {quote_style}
**Semicolons**: {semicolon_rule}

### Code Organization
**Imports**: {import_organization_rule}
```{language}
// External libraries
import React from 'react';
import axios from 'axios';

// Internal modules
import { UserService } from '../services';
import { validateInput } from '../utils';

// Relative imports
import './ComponentName.css';
```

## Enforcement
- Linter config: {linter_config_file}
- Formatter config: {formatter_config_file}
- Pre-commit hooks: {hook_status}

## Exceptions
These patterns have lower confidence and may need manual review:
- {exception_1}: {context_explanation}
- {exception_2}: {context_explanation}
```

### 7. Integration with Development Workflow

#### 7.1 Pre-Code Style Check
```python
def pre_code_style_check(target_language):
    """Load style rules before code generation"""
    
    # Query memory for style rules
    style_memories = search_memory(f"coding-style {target_language}")
    
    if not style_memories:
        return {
            "status": "no_rules_found",
            "recommendation": "run_style_analysis",
            "fallback": "use_language_defaults"
        }
    
    # Extract applicable rules
    applicable_rules = {}
    for memory in style_memories:
        category = memory["style_category"]
        applicable_rules[category] = memory["rules"]
    
    return {
        "status": "rules_loaded",
        "rules": applicable_rules,
        "confidence": calculate_overall_confidence(style_memories)
    }
```

#### 7.2 Real-time Style Application
```python
def apply_style_during_generation(code_snippet, language, style_rules):
    """Apply style rules during code generation"""
    
    styled_code = code_snippet
    
    # Apply naming conventions
    if "naming-conventions" in style_rules:
        styled_code = apply_naming_rules(styled_code, style_rules["naming-conventions"])
    
    # Apply formatting rules
    if "formatting" in style_rules:
        styled_code = apply_formatting_rules(styled_code, style_rules["formatting"])
    
    # Apply organization rules
    if "code-organization" in style_rules:
        styled_code = apply_organization_rules(styled_code, style_rules["code-organization"])
    
    return styled_code
```

### 8. Continuous Style Learning

#### 8.1 Style Pattern Updates
```python
def update_style_patterns(new_code_files):
    """Update style patterns based on new code"""
    
    # Analyze new files for style patterns
    new_patterns = analyze_style_patterns(new_code_files)
    
    # Compare with existing patterns
    existing_patterns = load_style_memories()
    
    # Update confidence scores
    updated_patterns = merge_pattern_confidence(existing_patterns, new_patterns)
    
    # Update memory entries
    for pattern in updated_patterns:
        if pattern["confidence_changed"] > 0.05:  # Significant change
            update_memory(pattern["memory_id"], pattern["new_data"])
    
    return updated_patterns
```

### 9. Error Handling and Edge Cases

#### 9.1 Insufficient Data Handling
```python
def handle_insufficient_style_data(language, file_count):
    """Handle cases with too few files for reliable analysis"""
    
    if file_count < 5:
        return {
            "status": "insufficient_data",
            "recommendation": "use_language_defaults",
            "fallback_source": f"common_patterns_{language}",
            "note": f"Only {file_count} files found, analysis unreliable"
        }
    
    if file_count < 20:
        return {
            "status": "limited_data",
            "recommendation": "low_confidence_rules",
            "confidence_modifier": 0.7,  # Reduce confidence by 30%
            "note": f"Analysis based on {file_count} files, may not represent full project"
        }
    
    return {"status": "sufficient_data"}
```

#### 9.2 Conflicting Pattern Resolution
```python
def resolve_conflicting_patterns(pattern_conflicts):
    """Resolve cases where multiple patterns have similar confidence"""
    
    resolutions = []
    
    for conflict in pattern_conflicts:
        if conflict["confidence_difference"] < 0.1:  # Very close patterns
            resolution = {
                "approach": "manual_review_required",
                "options": conflict["competing_patterns"],
                "suggestion": "analyze_context_factors",
                "recommendation": select_most_recent_pattern(conflict)
            }
        else:
            resolution = {
                "approach": "use_highest_confidence",
                "selected_pattern": conflict["highest_confidence_pattern"],
                "justification": "clear_statistical_preference"
            }
        
        resolutions.append(resolution)
    
    return resolutions
```

This style analysis task provides comprehensive instructions for extracting and documenting coding conventions to ensure consistent code generation that matches existing project patterns.