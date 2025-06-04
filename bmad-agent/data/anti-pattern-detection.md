# Anti-Pattern Detection Framework

## Overview

The BMAD Anti-Pattern Detection Framework implements zero-tolerance enforcement for behavioral violations with graduated penalties. This system actively prevents common AI interaction failures through pattern recognition and immediate consequences.

## Core Anti-Patterns

### Critical Violations ($5,000-$10,000 penalties)

#### 1. Vague Language Patterns
- **Pattern**: "I think", "probably", "maybe", "should work"
- **Penalty**: -$5,000
- **Detection**: Language uncertainty markers
- **Alternative**: "Based on [evidence], the solution is [specific]"

#### 2. Security Vulnerabilities
- **Pattern**: Hardcoded credentials, exposed keys, SQL injection risks
- **Penalty**: -$10,000
- **Detection**: Code pattern analysis
- **Alternative**: Environment variables, parameterized queries, validation

#### 3. Data Loss Risks
- **Pattern**: Destructive operations without backups, cascade deletes
- **Penalty**: -$10,000
- **Detection**: Operation impact analysis
- **Alternative**: Backup strategies, soft deletes, confirmation steps

#### 4. Production Failures
- **Pattern**: "Quick hack", "temporary fix", bypassing validation
- **Penalty**: -$8,000
- **Detection**: Code quality indicators
- **Alternative**: Proper implementation with tests

### Major Violations ($2,000-$5,000 penalties)

#### 5. Architecture Anti-Patterns
- **Pattern**: "Latest trend", premature optimization, over-engineering
- **Penalty**: -$3,000
- **Detection**: Technology choice reasoning
- **Alternative**: Evidence-based decisions with benchmarks

#### 6. Quality Shortcuts
- **Pattern**: "Skip tests", "TODO later", missing error handling
- **Penalty**: -$2,500
- **Detection**: Implementation completeness
- **Alternative**: Test-driven development, comprehensive error handling

#### 7. Performance Ignorance
- **Pattern**: "Performance doesn't matter", N+1 queries, memory leaks
- **Penalty**: -$2,000
- **Detection**: Performance impact analysis
- **Alternative**: Profiling, optimization, monitoring

#### 8. Documentation Negligence
- **Pattern**: "Code is self-documenting", missing API docs, no decision rationale
- **Penalty**: -$1,500
- **Detection**: Documentation coverage analysis
- **Alternative**: Comprehensive documentation with examples

### Moderate Violations ($500-$2,000 penalties)

#### 9. Unclear Requirements
- **Pattern**: "Make it better", "improve performance", "fix the bugs"
- **Penalty**: -$1,000
- **Detection**: Requirement specificity analysis
- **Alternative**: Specific, measurable requirements with acceptance criteria

#### 10. Poor Communication
- **Pattern**: Technical jargon without explanation, assumption of knowledge
- **Penalty**: -$750
- **Detection**: Communication clarity analysis
- **Alternative**: Clear explanations with examples

#### 11. Inconsistent Patterns
- **Pattern**: Mixed coding styles, varying naming conventions
- **Penalty**: -$500
- **Detection**: Consistency analysis
- **Alternative**: Established style guides and linting

#### 12. Resource Waste
- **Pattern**: Inefficient algorithms, unused imports, redundant code
- **Penalty**: -$750
- **Detection**: Efficiency analysis
- **Alternative**: Optimized implementations, code cleanup

### Minor Violations ($100-$500 penalties)

#### 13. Naming Violations
- **Pattern**: Single letter variables, unclear function names
- **Penalty**: -$200
- **Detection**: Naming convention analysis
- **Alternative**: Descriptive, intention-revealing names

#### 14. Code Smells
- **Pattern**: Long functions, deep nesting, magic numbers
- **Penalty**: -$300
- **Detection**: Code complexity analysis
- **Alternative**: Refactored, clean code patterns

#### 15. Missing Context
- **Pattern**: Solutions without explaining reasoning
- **Penalty**: -$150
- **Detection**: Context presence analysis
- **Alternative**: Solutions with clear rationale

#### 16. Version Control Violations
- **Pattern**: Massive commits, unclear commit messages
- **Penalty**: -$100
- **Detection**: Commit pattern analysis
- **Alternative**: Atomic commits with clear messages

## Detection Mechanisms

### Pattern Matching Rules
```yaml
vague_language:
  patterns: ["I think", "probably", "maybe", "should work", "might"]
  penalty: -5000
  context_required: true

security_risks:
  patterns: ["password =", "api_key =", "SELECT * FROM", "eval("]
  penalty: -10000
  blocking: true

quality_shortcuts:
  patterns: ["TODO", "FIXME", "quick hack", "temporary"]
  penalty: -2500
  escalation: true
```

### Context-Aware Detection
- **Project Phase**: Stricter rules during production deployment
- **Team Experience**: Adjusted penalties for junior vs senior teams
- **Time Pressure**: Emergency mode reduces some penalty severity
- **Technical Stack**: Technology-specific pattern rules

### Severity Classification
- **BLOCKING**: Prevents execution (security, data loss)
- **ESCALATING**: Increases penalty for repeated violations
- **WARNING**: Flags for review but allows execution
- **LEARNING**: Educational feedback with minimal penalty

## Prevention Strategies

### Proactive Warnings
```yaml
before_execution:
  - scan_for_patterns: true
  - confidence_threshold: 0.8
  - alternative_suggestions: required
  - user_confirmation: blocking_violations
```

### Alternative Approach Suggestions
- **Vague → Specific**: "Based on performance benchmarks..."
- **Quick Fix → Proper Solution**: "Implement with comprehensive tests..."
- **Assumption → Validation**: "Verify with user research data..."

### Learning from Near-Misses
- **Pattern Evolution**: Update rules based on new violations
- **Context Learning**: Adapt rules to project-specific needs
- **Success Tracking**: Reinforce patterns that prevent issues

## Penalty Framework

### Monetary System
```yaml
penalty_structure:
  critical: -5000 to -10000
  major: -2000 to -5000
  moderate: -500 to -2000
  minor: -100 to -500

escalation_rules:
  repeat_violation: penalty * 1.5
  rapid_succession: penalty * 2.0
  ignore_warnings: penalty * 3.0
```

### Positive Reinforcement
```yaml
rewards:
  pattern_avoidance: +500
  proactive_improvement: +1000
  teaching_others: +2000
  innovation_within_rules: +5000
```

### Behavioral Shaping
- **Immediate Feedback**: Penalties applied instantly
- **Clear Consequences**: Direct link between action and penalty
- **Consistent Application**: Same rules for all team members
- **Recovery Opportunities**: Ways to earn back through excellence

## Enforcement Integration

### Pre-Execution Validation
```python
def validate_before_execution(action, context):
    violations = detect_patterns(action)
    if has_blocking_violations(violations):
        return BLOCK_EXECUTION
    
    if has_major_violations(violations):
        penalty = calculate_penalty(violations)
        warn_user(penalty, suggest_alternatives(violations))
        return REQUIRE_CONFIRMATION
    
    return ALLOW_EXECUTION
```

### Runtime Monitoring
- **Continuous Scanning**: Monitor outputs for emerging patterns
- **Quality Gates**: Validate at key checkpoints
- **Team Metrics**: Track violation trends across team
- **Learning Loop**: Update rules based on outcomes

### Quality Assurance
- **Brotherhood Review**: Peer validation of penalty applications
- **Appeal Process**: Mechanism for challenging penalties
- **Pattern Refinement**: Regular review and improvement of rules
- **Success Measurement**: Track reduction in violations over time

## Pattern Library Updates

### Community Contributions
- **Crowd-Sourced Patterns**: Teams contribute new anti-patterns
- **Validation Process**: Peer review of proposed patterns
- **Effectiveness Tracking**: Measure pattern detection success
- **Global Learning**: Share successful patterns across teams

### Automatic Discovery
- **Failure Analysis**: Analyze incidents to identify new patterns
- **Code Review Mining**: Extract patterns from review comments
- **Issue Tracking**: Convert bug reports into prevention rules
- **Performance Monitoring**: Identify performance anti-patterns

## Success Metrics

### Violation Reduction
- **Target**: 95% reduction in critical violations within 3 months
- **Measurement**: Weekly violation counts by severity
- **Trend Analysis**: Month-over-month improvement tracking
- **Team Comparison**: Best practice sharing across teams

### Quality Improvement
- **Code Quality**: Increased review scores and reduced defects
- **Delivery Speed**: Faster delivery through fewer rework cycles
- **Team Learning**: Measured improvement in pattern recognition
- **Customer Satisfaction**: Fewer production issues

### Pattern Effectiveness
- **Detection Accuracy**: >90% true positive rate
- **False Positive Rate**: <5% incorrect pattern matches
- **Coverage**: All critical anti-patterns have detection rules
- **Response Time**: <200ms pattern detection latency

## Implementation Guidelines

### Team Onboarding
1. **Pattern Education**: Training on common anti-patterns
2. **Tool Integration**: IDE plugins for real-time detection
3. **Gradual Rollout**: Start with warnings, progress to penalties
4. **Feedback Collection**: Gather team input on pattern effectiveness

### Customization
- **Domain-Specific Rules**: Industry or technology specific patterns
- **Team Culture Adaptation**: Adjust penalties to team preferences
- **Project Phase Rules**: Different rules for MVP vs production
- **Legacy Code Handling**: Special rules for brownfield projects

### Continuous Improvement
- **Weekly Reviews**: Team discussion of violations and improvements
- **Monthly Pattern Updates**: Add new patterns based on learnings
- **Quarterly Effectiveness Review**: Analyze and adjust penalty structure
- **Annual Framework Evolution**: Major updates based on industry changes

Remember: Anti-patterns are the enemy of quality. Zero tolerance for violations ensures consistent excellence and continuous learning.