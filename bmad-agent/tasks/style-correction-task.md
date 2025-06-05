# Style Correction Task

## Purpose
Automatically detect style violations in existing code and apply corrections to match project-specific style patterns discovered during memory bootstrap or defined in project style guides.

## Behavioral Instructions

When user requests style correction or during automated code review:

### 1. Load Project Style Rules

```python
def load_project_style_rules(language, context="current-project"):
    """Load style rules from memory and project configuration"""
    
    # Query memory for style rules
    style_memories = search_memory(f"coding-style {language}")
    naming_memories = search_memory(f"naming-conventions {language}")
    formatting_memories = search_memory(f"formatting {language}")
    
    # Merge with project style guide if available
    project_style_guide = load_style_guide_if_exists()
    
    # Combine into comprehensive rule set
    return merge_style_rules([
        extract_rules_from_memories(style_memories),
        extract_rules_from_memories(naming_memories),
        extract_rules_from_memories(formatting_memories),
        project_style_guide
    ])
```

### 2. Style Violation Detection

#### 2.1 Automated Pattern Scanning
```python
def detect_style_violations(file_content, language, style_rules):
    """Scan code for style violations against established patterns"""
    
    violations = []
    
    # Naming convention violations
    naming_violations = check_naming_conventions(file_content, style_rules["naming"])
    violations.extend(naming_violations)
    
    # Formatting violations
    formatting_violations = check_formatting_rules(file_content, style_rules["formatting"])
    violations.extend(formatting_violations)
    
    # Code organization violations
    organization_violations = check_organization_patterns(file_content, style_rules["organization"])
    violations.extend(organization_violations)
    
    # Return ranked by severity and confidence
    return rank_violations_by_priority(violations)
```

#### 2.2 Violation Categories

**Critical Violations (Auto-Fix Required)**:
- Naming pattern inconsistencies
- Indentation/spacing errors
- Import organization violations
- Semicolon/quote consistency issues

**Warning Violations (Suggest Fix)**:
- Function length exceeded
- Comment style inconsistencies
- Variable naming clarity issues
- Organization pattern deviations

**Info Violations (Track Only)**:
- Minor formatting preferences
- Non-critical spacing issues
- Alternative pattern usage

### 3. Automatic Style Correction

#### 3.1 Safe Corrections
```python
def apply_safe_corrections(file_content, violations, style_rules):
    """Apply corrections that are guaranteed safe and reversible"""
    
    corrected_content = file_content
    applied_corrections = []
    
    for violation in violations:
        if violation["safety_level"] == "safe":
            if violation["type"] == "naming_convention":
                corrected_content = fix_naming_violation(
                    corrected_content, 
                    violation, 
                    style_rules["naming"]
                )
            elif violation["type"] == "formatting":
                corrected_content = fix_formatting_violation(
                    corrected_content, 
                    violation, 
                    style_rules["formatting"]
                )
            elif violation["type"] == "import_organization":
                corrected_content = fix_import_organization(
                    corrected_content,
                    violation,
                    style_rules["organization"]
                )
            
            applied_corrections.append(violation)
    
    return corrected_content, applied_corrections
```

#### 3.2 Language-Specific Corrections

**JavaScript/TypeScript Corrections**:
```typescript
// BEFORE: Style violations
import {UserService} from"../services/user";
import React from'react';
import axios from "axios";

interface props{
user_id:string;
onUpdate:(user:any)=>void;
}

export default function userProfile(props:props){
const{user_id,onUpdate}=props;
const[userData,setUserData]=useState(null);

const HandleUpdate=()=>{
console.log("updating...");
onUpdate(userData);
}

return<div className="profile">
<button onClick={HandleUpdate}>Update</button>
</div>;
}

// AFTER: Automatic style correction applied
import React, { useState } from 'react';
import axios from 'axios';

import { UserService } from '../services/user';

interface IUserProfileProps {
  userId: string;
  onUpdate: (user: UserData) => void;
}

export const UserProfileComponent: React.FC<IUserProfileProps> = ({
  userId,
  onUpdate
}) => {
  const [userData, setUserData] = useState<UserData | null>(null);

  const handleUserUpdate = (): void => {
    logger.info('Processing user update', { userId });
    onUpdate(userData);
  };

  return (
    <div className="user-profile">
      <button onClick={handleUserUpdate}>Update</button>
    </div>
  );
};
```

**Python Corrections**:
```python
# BEFORE: Style violations
import os,sys
from django.db import models
import requests

class userProfile(models.Model):
    user_name=models.CharField(max_length=100)
    Email=models.EmailField()
    
    def GetUserData(self):
        return{"name":self.user_name,"email":self.Email}

def processUser(user_data):
    if user_data==None:
        return None
    return user_data.GetUserData()

# AFTER: Automatic style correction applied
import os
import sys

import requests
from django.db import models


class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def get_user_data(self):
        return {
            "name": self.user_name,
            "email": self.email
        }


def process_user(user_data):
    if user_data is None:
        return None
    return user_data.get_user_data()
```

### 4. Interactive Correction Mode

#### 4.1 User-Guided Corrections
```python
def interactive_style_correction(file_path, violations):
    """Present violations to user for approval before applying fixes"""
    
    print(f"🔍 Found {len(violations)} style violations in {file_path}")
    print("=" * 50)
    
    for i, violation in enumerate(violations, 1):
        print(f"\n{i}. {violation['type'].replace('_', ' ').title()}")
        print(f"   Line {violation['line']}: {violation['description']}")
        print(f"   Current: {violation['current_code']}")
        print(f"   Suggested: {violation['suggested_fix']}")
        print(f"   Confidence: {violation['confidence']}%")
        
        choice = input("Apply fix? (y/n/s=skip all): ").lower()
        
        if choice == 'y':
            apply_single_violation_fix(file_path, violation)
            print("   ✅ Applied")
        elif choice == 's':
            print("   ⏭️  Skipping remaining violations")
            break
        else:
            print("   ⏭️  Skipped")
```

#### 4.2 Batch Correction Mode
```python
def batch_style_correction(project_root, language=None, auto_fix=False):
    """Apply style corrections to multiple files"""
    
    files_to_process = find_files_for_correction(project_root, language)
    
    correction_summary = {
        "files_processed": 0,
        "violations_found": 0,
        "corrections_applied": 0,
        "manual_review_needed": 0
    }
    
    for file_path in files_to_process:
        print(f"Processing {file_path}...")
        
        file_violations = detect_style_violations_in_file(file_path)
        correction_summary["violations_found"] += len(file_violations)
        
        if auto_fix:
            safe_corrections = filter_safe_corrections(file_violations)
            apply_corrections(file_path, safe_corrections)
            correction_summary["corrections_applied"] += len(safe_corrections)
            
            manual_violations = filter_manual_review_needed(file_violations)
            if manual_violations:
                save_manual_review_list(file_path, manual_violations)
                correction_summary["manual_review_needed"] += len(manual_violations)
        else:
            # Interactive mode for each file
            interactive_style_correction(file_path, file_violations)
        
        correction_summary["files_processed"] += 1
    
    generate_correction_report(correction_summary)
```

### 5. Correction Validation

#### 5.1 Pre-Correction Safety Checks
```python
def validate_correction_safety(original_code, corrected_code, language):
    """Ensure corrections don't break functionality"""
    
    safety_checks = {
        "syntax_valid": False,
        "imports_intact": False,
        "exports_intact": False,
        "function_signatures_preserved": False,
        "semantic_equivalence": False
    }
    
    # Syntax validation
    try:
        parse_code(corrected_code, language)
        safety_checks["syntax_valid"] = True
    except SyntaxError as e:
        raise CorrectionError(f"Correction introduces syntax error: {e}")
    
    # Import/export preservation
    original_imports = extract_imports(original_code)
    corrected_imports = extract_imports(corrected_code)
    safety_checks["imports_intact"] = imports_functionally_equivalent(
        original_imports, corrected_imports
    )
    
    # Function signature preservation
    original_functions = extract_function_signatures(original_code)
    corrected_functions = extract_function_signatures(corrected_code)
    safety_checks["function_signatures_preserved"] = signatures_match(
        original_functions, corrected_functions
    )
    
    return safety_checks
```

#### 5.2 Post-Correction Verification
```python
def verify_corrections_applied(file_path, applied_corrections):
    """Verify that all intended corrections were properly applied"""
    
    current_content = read_file(file_path)
    verification_results = []
    
    for correction in applied_corrections:
        verification = {
            "correction_id": correction["id"],
            "applied_successfully": False,
            "verification_method": None,
            "notes": []
        }
        
        if correction["type"] == "naming_convention":
            verification["applied_successfully"] = verify_naming_correction(
                current_content, correction
            )
            verification["verification_method"] = "pattern_match"
        elif correction["type"] == "formatting":
            verification["applied_successfully"] = verify_formatting_correction(
                current_content, correction
            )
            verification["verification_method"] = "format_analysis"
        
        verification_results.append(verification)
    
    return verification_results
```

### 6. Style Memory Learning

#### 6.1 Correction Pattern Recognition
```python
def learn_from_corrections(applied_corrections, project_context):
    """Update style patterns based on correction success/failure"""
    
    learning_insights = []
    
    for correction in applied_corrections:
        if correction["user_approved"] and correction["applied_successfully"]:
            # Successful correction reinforces pattern
            pattern_insight = {
                "type": "style-pattern-reinforcement",
                "pattern": correction["pattern_applied"],
                "context": project_context,
                "confidence_boost": 0.1,
                "evidence": f"correction-applied-successfully-{correction['file']}"
            }
            learning_insights.append(pattern_insight)
        
        elif not correction["user_approved"]:
            # Rejected correction indicates pattern exception
            exception_insight = {
                "type": "style-pattern-exception",
                "pattern": correction["pattern_applied"],
                "context": correction["file_context"],
                "exception_reason": correction["rejection_reason"],
                "evidence": f"correction-rejected-{correction['file']}"
            }
            learning_insights.append(exception_insight)
    
    # Update memory with insights
    for insight in learning_insights:
        add_memory(insight)
```

### 7. Integration with Development Workflow

#### 7.1 Pre-Commit Hook Integration
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "🎨 Running style correction..."

# Get list of staged files
staged_files=$(git diff --cached --name-only --diff-filter=ACM)

# Apply style corrections to staged files
bmad_style_correction --files="$staged_files" --auto-fix-safe

# Check if any corrections were applied
if [ $? -eq 0 ]; then
    echo "✅ Style corrections applied automatically"
    # Re-stage corrected files
    git add $staged_files
else
    echo "⚠️  Manual style review needed - check .bmad/style-issues.md"
    exit 1
fi
```

#### 7.2 IDE Integration Commands
```yaml
ide_commands:
  fix_file_style:
    command: "/style-correct current-file"
    description: "Fix style violations in current file"
    keybinding: "Ctrl+Shift+F"
  
  check_file_style:
    command: "/style-check current-file"
    description: "Check for style violations without fixing"
    keybinding: "Ctrl+Shift+C"
  
  batch_style_fix:
    command: "/style-correct project --interactive"
    description: "Fix style violations across project"
    menu: "Tools > BMAD > Fix Project Style"
```

### 8. Error Handling and Recovery

#### 8.1 Correction Failure Recovery
```python
def handle_correction_failure(file_path, correction, error):
    """Handle cases where style correction fails"""
    
    failure_info = {
        "file": file_path,
        "correction": correction,
        "error": str(error),
        "timestamp": datetime.now(),
        "recovery_action": None
    }
    
    if isinstance(error, SyntaxError):
        # Syntax error - revert and flag for manual review
        revert_file_to_previous_state(file_path)
        failure_info["recovery_action"] = "reverted_to_original"
        add_to_manual_review_queue(file_path, correction, "syntax_error")
    
    elif isinstance(error, SemanticChangeError):
        # Semantic change detected - revert and update pattern confidence
        revert_file_to_previous_state(file_path)
        reduce_pattern_confidence(correction["pattern"], 0.2)
        failure_info["recovery_action"] = "reverted_pattern_confidence_reduced"
    
    elif isinstance(error, FileAccessError):
        # File access issue - retry later
        queue_for_retry(file_path, correction)
        failure_info["recovery_action"] = "queued_for_retry"
    
    # Log failure for learning
    log_correction_failure(failure_info)
    
    return failure_info
```

### 9. Reporting and Analytics

#### 9.1 Style Correction Report
```markdown
# Style Correction Report

## Summary
**Date**: {date}
**Project**: {project_name}
**Files Processed**: {files_count}
**Total Violations Found**: {violations_count}
**Corrections Applied**: {corrections_count}
**Manual Review Needed**: {manual_review_count}

## Violation Breakdown
| Type | Count | Auto-Fixed | Manual Review |
|------|-------|------------|---------------|
| Naming Conventions | {count} | {auto_fixed} | {manual} |
| Formatting | {count} | {auto_fixed} | {manual} |
| Import Organization | {count} | {auto_fixed} | {manual} |
| Code Structure | {count} | {auto_fixed} | {manual} |

## Most Common Violations
1. **{violation_type}**: {count} instances
   - Pattern: {pattern_description}
   - Fix Rate: {auto_fix_percentage}%
   - Examples: {file_examples}

## Files Requiring Manual Review
- {file_1}: {violation_types}
- {file_2}: {violation_types}

## Style Pattern Learning
- **Reinforced Patterns**: {reinforced_count}
- **New Exceptions Found**: {exceptions_count}
- **Confidence Updates**: {confidence_updates}

## Recommendations
1. {recommendation_1}
2. {recommendation_2}
3. {recommendation_3}
```

### 10. Command Interface

#### 10.1 Style Correction Commands
```yaml
style_correction_commands:
  check_style:
    command: "/style-check [file|project] [--language=<lang>]"
    description: "Check for style violations without applying fixes"
    
  fix_style:
    command: "/style-correct [file|project] [--auto|--interactive] [--safe-only]"
    description: "Apply style corrections to files"
    
  learn_style:
    command: "/style-learn [directory] [--update-memory]"
    description: "Analyze codebase and update style patterns"
    
  show_style_rules:
    command: "/style-rules [--language=<lang>] [--category=<cat>]"
    description: "Display current style rules and their confidence"
    
  reset_style_memory:
    command: "/style-reset [--language=<lang>] [--confirm]"
    description: "Reset learned style patterns (use with caution)"
```

This comprehensive style correction system ensures that code automatically conforms to discovered project patterns while providing safety mechanisms, learning capabilities, and integration with existing development workflows.