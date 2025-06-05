# Quality Gate Improvement Guidance

## Gate Failure Summary
**Gate**: {gate_name}  
**Phase**: {current_phase}  
**Trigger**: {trigger_type}  
**Failed At**: {timestamp}  
**Blocking Progress**: {yes/no}  
**Override Available**: {yes/no}

## Failed Checks Overview

| Check | Expected | Actual | Severity | Impact |
|-------|----------|--------|----------|---------|
| {check_1} | {expected_1} | {actual_1} | {severity_1} | {impact_1} |
| {check_2} | {expected_2} | {actual_2} | {severity_2} | {impact_2} |
| {check_3} | {expected_3} | {actual_3} | {severity_3} | {impact_3} |

**Total Checks**: {total_checks}  
**Passed**: {passed_checks}  
**Failed**: {failed_checks}  
**Gate Score**: {gate_score}%

## 🎯 Immediate Actions Required

### Priority 1: {most_critical_issue}
**Why This Matters**: {impact_explanation}  
**Quick Fix** (Est. {quick_fix_time}):
```
{quick_fix_steps}
```

### Priority 2: {second_critical_issue}
**Why This Matters**: {impact_explanation}  
**Quick Fix** (Est. {quick_fix_time}):
```
{quick_fix_steps}
```

## 💡 Root Cause Analysis

### Why Did This Happen?
{root_cause_analysis}

### Pattern Detection
Based on memory analysis, this type of failure:
- **Frequency**: Occurs in {frequency}% of similar situations
- **Common Cause**: {most_common_cause}
- **Team History**: Your team has encountered this {team_occurrence_count} times

## 📚 Memory-Based Solutions

### What Worked Before
**Similar Situation**: {similar_context}  
**Resolution Applied**: {previous_resolution}  
**Time to Fix**: {historical_fix_time}  
**Success Rate**: {success_percentage}%

```
# Example from {example_project}
{code_example_that_worked}
```

### Team-Specific Patterns
Your team typically resolves this by:
1. {team_pattern_1}
2. {team_pattern_2}
3. {team_pattern_3}

## 🔧 Recommended Solution Path

### Step-by-Step Resolution
**Estimated Total Time**: {total_estimated_time}

#### Step 1: {first_step_title} (⏱️ {step_1_time})
{detailed_step_1_instructions}

**Verification**:
```bash
{verification_command_1}
```

#### Step 2: {second_step_title} (⏱️ {step_2_time})
{detailed_step_2_instructions}

**Verification**:
```bash
{verification_command_2}
```

#### Step 3: {third_step_title} (⏱️ {step_3_time})
{detailed_step_3_instructions}

**Verification**:
```bash
{verification_command_3}
```

## 🏆 Best Practices to Apply

### Industry Standards
For {failure_category}, industry best practices recommend:
- {best_practice_1}
- {best_practice_2}
- {best_practice_3}

### Project-Specific Standards
Based on your project's patterns:
- {project_standard_1}
- {project_standard_2}
- {project_standard_3}

## 🚀 Prevention Strategy

### How to Avoid This in Future
1. **Pre-commit Checks**: Add {suggested_pre_commit_check}
2. **Development Practice**: Implement {suggested_practice}
3. **Team Process**: Establish {suggested_process}

### Automated Prevention
```yaml
# Add to your quality gate configuration
preventive_checks:
  {check_type}:
    trigger: "pre_commit"
    threshold: {recommended_threshold}
    enforcement: "strict"
```

## 📊 Similar Issues & Resolutions

### Recent Team Resolutions
| Date | Issue | Resolution | Time to Fix | Prevented Recurrence |
|------|-------|------------|-------------|---------------------|
| {date_1} | {issue_1} | {resolution_1} | {time_1} | {prevented_1} |
| {date_2} | {issue_2} | {resolution_2} | {time_2} | {prevented_2} |

### Cross-Project Learnings
Teams solving similar issues found success with:
- **{team_a}**: {approach_a} (Success: {success_a}%)
- **{team_b}**: {approach_b} (Success: {success_b}%)
- **{team_c}**: {approach_c} (Success: {success_c}%)

## ⏱️ Time Investment Analysis

### Fix Now vs Fix Later
**Fix Now**:
- Time Required: {immediate_fix_time}
- Benefits: {immediate_benefits}
- Risk Avoided: {avoided_risks}

**Defer Fix** (if override available):
- Technical Debt Created: {debt_description}
- Future Time Required: {future_fix_time} (typically {multiplier}x longer)
- Compound Risk: {compound_risk_description}

## 🔄 Next Steps

### After Fixing Issues
1. Run gate check again: `/gate-check {trigger} --recheck`
2. Verify all checks pass: `/gate-status --detailed`
3. Document resolution: `/gate-resolution {gate_id} --notes "{what_fixed_it}"`

### If Override Needed
1. Review override requirements in next section
2. Prepare justification with business context
3. Submit override request: `/gate-override {gate_name} --reason "{justification}"`

## 📋 Quality Gate Re-check Command

Once you've implemented the fixes:
```bash
# Re-run the quality gate
/gate-check {original_trigger} --phase {current_phase}

# Or run specific checks
/gate-check --only "{failed_check_names}"
```

---

**Remember**: Quality gates exist to protect code quality and team velocity. Fixing issues now prevents larger problems later. The time invested in meeting quality standards pays dividends in reduced bugs, easier maintenance, and faster feature development.