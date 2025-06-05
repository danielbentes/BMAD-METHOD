# Quality Gate Examples

## Overview
Real-world examples demonstrating quality gate automation in action, including gate triggers, failure scenarios, improvement guidance, and override handling.

## Example 1: Pre-Commit Gate - Style Consistency Failure

### Scenario
Developer attempts to commit code with style violations and missing tests.

### Gate Trigger
```bash
$ git commit -m "Add user authentication feature"
🔍 Quality Gate: Pre-Commit Check Triggered
```

### Gate Execution
```yaml
Gate: pre_commit
Phase: Development
Trigger: code_staged
Enforcement: strict
Timestamp: 2024-01-06 14:23:15
```

### Check Results
```
❌ QUALITY GATE FAILED

Failed Checks:
1. ❌ Style Consistency: 78% (Required: ≥95%)
   - Mixed naming conventions detected
   - Inconsistent import organization
   - Formatting deviations from project standard

2. ❌ Unit Tests: 0% (Required: 100%)
   - No tests found for new authentication module
   - Critical paths lack coverage

3. ✅ Linting: Passed (0 violations)
4. ✅ Type Checking: Passed (0 errors)

Gate Score: 50% (2/4 checks passed)
Status: BLOCKED - Cannot commit
```

### Improvement Guidance Generated
```markdown
## 🎯 Immediate Actions Required

### Priority 1: Add Unit Tests (Est. 45 mins)
Why This Matters: Zero test coverage blocks all commits
Quick Fix:
1. Create test file: tests/test_authentication.py
2. Add basic test structure:
   ```python
   import pytest
   from src.auth import authenticate_user, create_token

   def test_authenticate_valid_user():
       result = authenticate_user("valid@email.com", "password")
       assert result.success == True
       assert result.token is not None

   def test_authenticate_invalid_user():
       result = authenticate_user("invalid@email.com", "wrong")
       assert result.success == False
   ```

### Priority 2: Fix Style Consistency (Est. 20 mins)
Why This Matters: Project maintains 95%+ style consistency
Quick Fix:
1. Run automatic style correction:
   ```bash
   /style-correct src/auth --auto-fix-safe
   ```
2. Manual fixes needed:
   - Rename `getUserData` to `get_user_data` (line 45)
   - Reorganize imports: external → internal → local

## 💡 Based on Team History
Your team typically resolves style issues by:
1. Running auto-formatter first (85% success rate)
2. Manual review for naming (15 mins average)
3. Import reorganization tool (5 mins)

Previous similar fix by TeamMemberA took 35 minutes total.
```

### Developer Response
```bash
# Developer runs suggested fixes
$ /style-correct src/auth --auto-fix-safe
✅ Fixed 15 style violations automatically
⚠️  3 violations require manual intervention

$ pytest tests/test_authentication.py
✅ All tests passing (6/6)

# Retry commit
$ git commit -m "Add user authentication feature"
🔍 Quality Gate: Pre-Commit Check Triggered
✅ QUALITY GATE PASSED
✅ Commit successful
```

## Example 2: Architecture Phase Exit - Missing Analysis Tag

### Scenario
Architect completes architecture design but forgets required analysis tag.

### Gate Trigger
```bash
$ /workflow complete-phase architecture
🔍 Quality Gate: Architecture Phase Exit Triggered
```

### Check Results
```
❌ QUALITY GATE FAILED

Failed Checks:
1. ❌ Architecture Analysis Tag: NOT FOUND (Required: Present)
   - No <architecture_analysis> tag in decisions
   - Missing structured thinking documentation

2. ✅ Scalability Design: 92% (Required: ≥90%)
3. ✅ Security Architecture: 96% (Required: ≥95%)
4. ✅ Performance Planning: 88% (Required: ≥85%)
5. ✅ Component Boundaries: 97% (Required: ≥95%)

Gate Score: 80% (4/5 checks passed)
Status: BLOCKED - Cannot complete phase
Enforcement: STRICT - No override available
```

### Immediate Remediation
```markdown
## Required Action: Add Architecture Analysis

Your architecture decisions must include structured analysis:

```xml
<architecture_analysis>
  <current_state>
    <!-- Analyze existing system if applicable -->
  </current_state>
  
  <proposed_architecture>
    <!-- Detailed proposed architecture -->
  </proposed_architecture>
  
  <alternatives_considered>
    <!-- Other options evaluated -->
  </alternatives_considered>
  
  <trade_offs>
    <!-- Pros/cons of chosen approach -->
  </trade_offs>
  
  <decision_rationale>
    <!-- Why this architecture was selected -->
  </decision_rationale>
  
  <risk_assessment>
    <!-- Architectural risks and mitigations -->
  </risk_assessment>
</architecture_analysis>
```

Add this analysis to your architecture document and retry phase completion.
```

### Resolution
Architect adds required analysis tag with comprehensive content, gate passes on retry.

## Example 3: Story Completion - Test Coverage Below Threshold

### Scenario
Developer marks story as complete, but test coverage is insufficient.

### Gate Trigger
```bash
$ /story complete AUTH-123
🔍 Quality Gate: Story Completion Check Triggered
```

### Check Results
```
❌ QUALITY GATE FAILED

Failed Checks:
1. ❌ Test Coverage: 72% (Required: ≥85%)
   - Uncovered lines: 45-67, 89-95, 112-134
   - Critical paths missing: error handling, edge cases

2. ✅ DoD Checklist: 100% (Complete)
3. ✅ Code Review: Approved
4. ✅ Integration Tests: 100% Passing

Gate Score: 75% (3/4 checks passed)
Status: BLOCKED - Cannot close story
```

### Memory-Based Guidance
```markdown
## 📚 Similar Issues From Memory

### Team Pattern Detected
Your team encountered low test coverage 3 times last sprint:
- Resolution Time: Average 2.5 hours
- Common Cause: Missing edge case tests
- Success Pattern: Focus on error paths first

### Suggested Test Cases
Based on your code analysis, add tests for:

1. **Error Handling** (lines 45-67)
   ```python
   def test_auth_database_connection_error():
       with mock.patch('db.connect', side_effect=ConnectionError):
           result = authenticate_user("user@test.com", "pass")
           assert result.error == "Service temporarily unavailable"
   ```

2. **Edge Cases** (lines 89-95)
   ```python
   def test_auth_empty_credentials():
       assert authenticate_user("", "").error == "Invalid credentials"
       assert authenticate_user(None, None).error == "Invalid credentials"
   ```

3. **Token Expiry** (lines 112-134)
   ```python
   def test_token_expiry_handling():
       expired_token = create_token(user_id=1, expires_in=-1)
       assert validate_token(expired_token).valid == False
   ```

Expected coverage after adding these: 87% ✅
```

## Example 4: Sprint End Gate - Technical Debt Exceeded

### Scenario
Sprint ends with technical debt ratio above acceptable threshold.

### Gate Trigger
```bash
$ /sprint close SPRINT-15
🔍 Quality Gate: Sprint End Check Triggered
```

### Check Results
```
⚠️ QUALITY GATE WARNING

Failed Checks:
1. ❌ Technical Debt Ratio: 76% (Required: ≥85%)
   - New debt added: 12 items
   - Debt resolved: 3 items
   - Debt growth rate: 300%

2. ✅ Sprint Goals: 92% achieved
3. ✅ Performance Baseline: 96% maintained

Gate Score: 67% (2/3 checks passed)
Status: WARNING - Sprint can close with conditions
Enforcement: STANDARD - Override available
```

### Override Request Generated
```yaml
Override Request: QG-OVERRIDE-2024-0042
Requester: John Smith (Scrum Master)
Gate: sprint_end
Reason: Customer demo deadline

Business Justification:
- Critical customer demo scheduled for Monday
- 3 features must be delivered for contract
- Debt items are internal refactoring only
- No customer-facing impact

Risk Assessment:
- Probability: Medium (60%)
- Impact: Low (performance may degrade 5-10%)
- Mitigation: Dedicated debt sprint planned next

Remediation Commitment:
- Sprint 16 will be 50% debt reduction
- Specific stories created: TECH-234 through TECH-245
- Target debt ratio: 92% by Sprint 16 end

Accountability: John Smith
Approval Required: Tech Lead
```

### Override Approval
```
Override Status: APPROVED with conditions
Approved By: Sarah Chen (Tech Lead)
Conditions:
1. Daily debt metrics review in Sprint 16
2. No new features until debt ratio > 85%
3. Performance monitoring enabled
4. Escalate if performance degrades > 5%

Technical Debt Ticket: TECH-233
Remediation Deadline: 2024-01-20 (Sprint 16 end)
```

## Example 5: Critical Change Gate - Security Component Modified

### Scenario
Developer modifies authentication encryption algorithm.

### Gate Trigger
```bash
$ git push origin feature/update-encryption
🔍 Quality Gate: Security Component Change Triggered
🚨 CRITICAL GATE - STRICT ENFORCEMENT
```

### Check Results
```
❌ CRITICAL SECURITY GATE FAILED

Failed Checks:
1. ❌ Security Scan: 2 vulnerabilities detected
   - CVE-2024-1234: Weak key derivation
   - CWE-327: Use of broken crypto algorithm

2. ❌ Security Review: Not completed
   - Required: Security team approval
   - Status: Review not requested

3. ✅ Audit Logging: Changes logged
4. ⚠️ Penetration Test: Not applicable (pre-merge)

Gate Score: 25% (1/4 checks passed)
Status: BLOCKED - CANNOT PROCEED
Enforcement: STRICT - NO OVERRIDE POSSIBLE
```

### Mandatory Actions
```markdown
## 🛑 SECURITY GATE - IMMEDIATE ACTION REQUIRED

### Critical Issues Must Be Resolved:

1. **Fix Security Vulnerabilities**
   ```python
   # VULNERABLE CODE (current):
   key = hashlib.md5(password).hexdigest()  # MD5 is broken
   
   # REQUIRED FIX:
   key = hashlib.pbkdf2_hmac(
       'sha256',
       password.encode('utf-8'),
       salt,
       100000  # iterations
   )
   ```

2. **Request Security Review**
   ```bash
   /security request-review --priority=critical \
     --component=authentication \
     --changes="encryption algorithm update"
   ```

3. **Update Security Documentation**
   - Document algorithm choice rationale
   - Update threat model
   - Add security test cases

### No Alternative Path
This gate cannot be overridden. Security vulnerabilities must be fixed before any progress is possible.
```

## Example 6: Milestone Gate - 50% Complete Quality Check

### Scenario
Project reaches 50% completion milestone, automatic quality assessment triggered.

### Gate Trigger
```bash
Project Analytics: 50% stories completed
🔍 Quality Gate: 50% Milestone Check Triggered
```

### Check Results
```
✅ QUALITY GATE PASSED WITH OBSERVATIONS

Check Results:
1. ✅ Feature Completion: 48% (Required: ≥45%)
2. ✅ Integration Stability: 88% (Required: ≥85%)
3. ⚠️ Quality Trend: 87% (Required: ≥90%)
   - Declining test coverage trend
   - Increasing code complexity

Gate Score: 87% (2/3 full pass, 1 warning)
Status: PASSED - Continue with monitoring
```

### Proactive Guidance
```markdown
## 📈 Quality Trend Analysis

### Concerning Pattern Detected
Quality metrics show gradual decline:
- Week 1: 95% quality score
- Week 2: 92% quality score
- Week 3: 89% quality score
- Week 4: 87% quality score (current)

### Predicted Issues (Based on Memory)
Similar patterns in past projects led to:
- 75% chance of major refactoring at 75% milestone
- 60% chance of performance issues in integration
- 45% chance of deadline slip

### Recommended Preventive Actions
1. **Immediate**: Dedicate next sprint 20% to quality
2. **This Week**: Review and refactor complex modules
3. **Ongoing**: Add complexity checks to pre-commit gates

### Success Pattern from ProjectX
ProjectX reversed similar trend by:
- Daily 15-min quality reviews
- Pairing on complex features
- Automated complexity warnings
Result: Quality improved to 94% by 75% milestone
```

## Key Patterns Observed

### Successful Gate Passages
1. **Preparation**: Teams that run local checks first have 85% higher pass rate
2. **Incremental**: Frequent small commits pass 3x more often than large changes
3. **Memory Usage**: Teams using improvement guidance resolve issues 60% faster

### Common Failure Patterns
1. **Rush Commits**: End-of-day commits fail 4x more often
2. **Skip Local Checks**: 70% of failures could be caught locally
3. **Ignore Warnings**: Advisory gates ignored become blocking issues

### Override Patterns
1. **Justified Overrides**: 90% meet remediation commitments
2. **Unjustified Overrides**: Lead to 3x more future failures
3. **Team Learning**: Override frequency decreases 40% after 3 months

These examples demonstrate how quality gates work in practice to maintain high standards while providing helpful guidance for continuous improvement.