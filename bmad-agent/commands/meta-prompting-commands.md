# Meta-Prompting Commands

## User Commands

### `/meta-prompt generate [type]`
Generate an optimal prompt for a specific task or agent.

**Parameters:**
- `type`: Type of prompt to generate (task|persona|consultation|analysis)

**Options:**
- `--context [details]`: Additional context for customization
- `--optimize [target]`: Optimization focus (clarity|tokens|effectiveness)
- `--preview`: Show prompt before deployment

**Examples:**
```
/meta-prompt generate task --context "code review for legacy system"
/meta-prompt generate consultation --context "design review"
/meta-prompt generate persona --context "architect for microservices"
```

### `/meta-prompt test [prompt]`
Test a generated prompt and measure effectiveness.

**Parameters:**
- `prompt`: Prompt ID or inline prompt to test

**Options:**
- `--metrics`: Show detailed effectiveness metrics
- `--compare [baseline]`: Compare against baseline prompt
- `--iterations [n]`: Run multiple test iterations

**Examples:**
```
/meta-prompt test prompt-123 --metrics
/meta-prompt test "You are a code reviewer..." --compare baseline
```

### `/meta-prompt patterns`
Show successful prompt patterns from the library.

**Options:**
- `--type [category]`: Filter by pattern type
- `--success-rate [min]`: Show only high-performing patterns
- `--recent`: Show recently successful patterns

**Examples:**
```
/meta-prompt patterns --type task-execution
/meta-prompt patterns --success-rate 90
/meta-prompt patterns --recent
```

### `/meta-prompt optimize`
Optimize existing prompts based on performance data.

**Options:**
- `--target [prompt-id]`: Specific prompt to optimize
- `--all`: Optimize all prompts in system
- `--dry-run`: Preview optimizations without applying

**Examples:**
```
/meta-prompt optimize --target persona-architect
/meta-prompt optimize --all --dry-run
```

## System Commands

### `/meta-prompt effectiveness`
Display effectiveness metrics for meta-prompting system.

**Output:**
- Task completion rates by prompt type
- Output quality scores
- Token efficiency gains
- Error reduction percentages

### `/meta-prompt library`
Access the prompt pattern library.

**Options:**
- `--add [pattern]`: Add successful pattern
- `--rate [id] [score]`: Rate pattern effectiveness
- `--export`: Export library for sharing

### `/meta-prompt debug [session]`
Debug prompt generation for a specific session.

**Parameters:**
- `session`: Session ID to analyze

**Output:**
- Context analysis performed
- Template selection logic
- Adaptations applied
- Final prompt generated

## Integration Commands

### `/meta-prompt persona [name]`
Generate optimal activation prompt for a persona.

**Parameters:**
- `name`: Persona identifier (architect|pm|dev|etc)

**Options:**
- `--task [description]`: Include specific task context
- `--expertise [level]`: Adjust for team expertise
- `--constraints [list]`: Add specific constraints

### `/meta-prompt consultation [type]`
Generate multi-agent consultation prompt.

**Parameters:**
- `type`: Consultation type (design-review|technical|strategy)

**Options:**
- `--participants [list]`: Override default participants
- `--objectives [goals]`: Specify consultation goals
- `--time-box [minutes]`: Set time constraints

### `/meta-prompt handoff [from] [to]`
Generate optimal handoff prompt between personas.

**Parameters:**
- `from`: Source persona
- `to`: Target persona

**Options:**
- `--context-level [0-3]`: How much context to transfer
- `--quality-gates`: Include quality validation
- `--continuity`: Emphasize task continuity

## Advanced Commands

### `/meta-prompt a/b [variant]`
Run A/B test for prompt variants.

**Parameters:**
- `variant`: New prompt variant to test

**Options:**
- `--baseline [id]`: Baseline for comparison
- `--metrics [list]`: Specific metrics to track
- `--duration [time]`: Test duration

### `/meta-prompt learn`
Analyze recent prompt performance and update patterns.

**Options:**
- `--period [days]`: Analysis period (default: 7)
- `--threshold [score]`: Learning threshold
- `--apply`: Apply learned improvements

### `/meta-prompt cascade`
Show how prompts cascade through system.

**Options:**
- `--from [source]`: Starting point
- `--depth [n]`: Cascade depth to show
- `--rules`: Show inheritance rules

## Usage Examples

### Generating Task Prompt
```
User: /meta-prompt generate task --context "refactor authentication system"

BMAD: Generated optimal task prompt:

You are tasked with refactoring the authentication system.

Context: Existing auth uses outdated patterns, needs modernization
Constraints: Maintain backward compatibility, zero downtime
Success Criteria: JWT implementation, refresh tokens, 2FA ready

MANDATORY SAFETY RULES:
- ZERO security vulnerabilities
- MUST maintain all existing integrations
- REQUIRE comprehensive test coverage

[Preview complete. Use --deploy to activate]
```

### Testing Prompt Effectiveness
```
User: /meta-prompt test prompt-123 --metrics

BMAD: Prompt effectiveness analysis:
- Task completion: 92% (target: 90%) ✓
- Output quality: 88% (target: 85%) ✓
- Token efficiency: 35% reduction ✓
- Clarifications needed: 1 (down from 3)

Success patterns identified:
- Clear success criteria improved completion
- Numbered steps reduced clarification needs
- Example inclusion increased quality
```

### Optimizing Prompts
```
User: /meta-prompt optimize --target persona-architect

BMAD: Optimization analysis for Architect persona:

Current performance:
- Effectiveness: 86%
- Common issues: Scope creep, over-engineering

Proposed optimizations:
1. Add constraint emphasis: "Start simple, evolve with need"
2. Include anti-pattern: "AVOID premature optimization"
3. Add success metric: "Decisions justified by data"

Expected improvement: +8% effectiveness
[Apply optimizations? y/n]
```

## Best Practices

1. **Test Before Deploy**: Always preview generated prompts
2. **Measure Effectiveness**: Track metrics for continuous improvement
3. **Context is Key**: Provide rich context for better generation
4. **Learn from Success**: Add successful patterns to library
5. **Iterate and Refine**: Use A/B testing for improvements

Remember: Great prompts create great outcomes. Meta-prompting multiplies this effect across the entire system.