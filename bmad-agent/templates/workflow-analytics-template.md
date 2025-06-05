# Workflow Analytics Template

## Workflow Performance Dashboard

**Generated**: {timestamp}  
**Workflow**: {workflow_name}  
**Analysis Period**: {start_date} to {end_date}  
**Total Cycles**: {completed_cycles}

---

## Executive Summary

### Key Metrics
- **Average Completion Time**: {avg_completion} days (vs typical: {typical_completion})
- **Efficiency Score**: {efficiency_score}/100
- **Success Rate**: {success_rate}%
- **Bottleneck Count**: {bottleneck_count}

### Performance Trend
```
Efficiency Score (Last 5 Cycles)
100 |         
 90 |     *   * 
 80 |   *   *   ← Current: {current_score}
 70 | *
 60 +---+---+---+---+---+
    C1  C2  C3  C4  C5
```

---

## Phase-by-Phase Analysis

### Phase Performance Table
| Phase | Avg Duration | Typical | Variance | Bottlenecks | Success Rate |
|-------|-------------|---------|----------|-------------|--------------|
| {phase_1} | {duration} | {typical} | {variance}% | {count} | {rate}% |
| {phase_2} | {duration} | {typical} | {variance}% | {count} | {rate}% |
| {phase_3} | {duration} | {typical} | {variance}% | {count} | {rate}% |
| {phase_4} | {duration} | {typical} | {variance}% | {count} | {rate}% |

### Phase Duration Visualization
```
{phase_1}    [████████░░] {duration}d (typical: {typical}d)
{phase_2}    [██████████] {duration}d (typical: {typical}d) ⚠️
{phase_3}    [███████░░░] {duration}d (typical: {typical}d)
{phase_4}    [█████░░░░░] {duration}d (typical: {typical}d) ✅
```

---

## Bottleneck Analysis

### Critical Bottlenecks Identified
1. **{bottleneck_1}**
   - Location: {phase} → {task}
   - Frequency: {frequency}% of cycles
   - Average Delay: {delay} days
   - Root Cause: {cause}
   - Resolution Pattern: {successful_resolution}

2. **{bottleneck_2}**
   - Location: {phase} → {task}
   - Frequency: {frequency}% of cycles
   - Average Delay: {delay} days
   - Root Cause: {cause}
   - Resolution Pattern: {successful_resolution}

### Bottleneck Impact Matrix
```
Impact
High  | B1    |       | B2
Med   |       | B3    |
Low   | B4    |       | B5
      +-------+-------+-------+
       Low    Med    High   Frequency
```

---

## Handoff Efficiency

### Handoff Performance
| From | To | Avg Duration | Success Rate | Info Loss | Improvement |
|------|----|-------------|--------------|-----------|-------------|
| {persona_1} | {persona_2} | {duration} | {rate}% | {loss}% | {trend} |
| {persona_2} | {persona_3} | {duration} | {rate}% | {loss}% | {trend} |
| {persona_3} | {persona_4} | {duration} | {rate}% | {loss}% | {trend} |

### Handoff Optimization Opportunities
- **{handoff_1}**: {optimization_suggestion}
- **{handoff_2}**: {optimization_suggestion}
- **{handoff_3}**: {optimization_suggestion}

---

## Resource Utilization

### Persona Activity Distribution
```
{persona_1}  [████████░░░░░░] 35% - Primary: {main_tasks}
{persona_2}  [██████░░░░░░░░] 25% - Primary: {main_tasks}
{persona_3}  [████░░░░░░░░░░] 20% - Primary: {main_tasks}
{persona_4}  [███░░░░░░░░░░░] 15% - Primary: {main_tasks}
Other        [█░░░░░░░░░░░░░]  5%
```

### Resource Efficiency Insights
- **Underutilized**: {underutilized_resources}
- **Overloaded**: {overloaded_resources}
- **Optimal Balance**: {balanced_resources}

---

## Quality Metrics

### Quality Gate Performance
| Gate | Pass Rate | Avg Rework | Trend | Common Issues |
|------|-----------|------------|-------|---------------|
| {gate_1} | {rate}% | {rework}h | {trend} | {issues} |
| {gate_2} | {rate}% | {rework}h | {trend} | {issues} |
| {gate_3} | {rate}% | {rework}h | {trend} | {issues} |

### Quality Trends
```
Pass Rate % (Last 10 Gates)
100 |       *   *
 90 | * * *   *   * ← Current: {current}%
 80 |       *
 70 +---+---+---+---+---+---+---+---+---+---+
    G1 G2 G3 G4 G5 G6 G7 G8 G9 G10
```

---

## Success Pattern Analysis

### Top Success Patterns
1. **{pattern_1}**
   - Frequency: Used in {frequency}% of successful cycles
   - Impact: {time_saved} average time reduction
   - Context: {when_applicable}
   - Key Factor: {success_factor}

2. **{pattern_2}**
   - Frequency: Used in {frequency}% of successful cycles
   - Impact: {quality_improvement} quality improvement
   - Context: {when_applicable}
   - Key Factor: {success_factor}

3. **{pattern_3}**
   - Frequency: Used in {frequency}% of successful cycles
   - Impact: {efficiency_gain} efficiency gain
   - Context: {when_applicable}
   - Key Factor: {success_factor}

### Pattern Adoption Recommendations
Based on analysis, adopting these patterns could yield:
- **Time Savings**: {estimated_time_saved} per cycle
- **Quality Improvement**: {estimated_quality_gain}
- **Cost Reduction**: {estimated_cost_reduction}

---

## Comparative Analysis

### Team Comparison
```
Your Team vs Department Average

Efficiency    [████████░░] 85% vs 78% (+7%)
Speed         [███████░░░] 75% vs 80% (-5%)
Quality       [█████████░] 92% vs 85% (+7%)
Innovation    [████████░░] 88% vs 82% (+6%)
```

### Historical Performance
```
Efficiency Trend (Last 6 Months)
100 |           
 90 |       * * ← Current
 80 |   * *
 70 | *
 60 +---+---+---+---+---+---+
    M1  M2  M3  M4  M5  M6
```

---

## Predictive Analytics

### Next Cycle Predictions
Based on current patterns and historical data:

- **Expected Duration**: {predicted_duration} days (confidence: {confidence}%)
- **Likely Bottlenecks**: {predicted_bottlenecks}
- **Risk Areas**: {risk_areas}
- **Success Probability**: {success_probability}%

### Optimization Impact Forecast
If recommended optimizations are implemented:
- **Time Reduction**: {time_impact}%
- **Quality Improvement**: {quality_impact}%
- **Bottleneck Reduction**: {bottleneck_impact}%

---

## Actionable Recommendations

### Immediate Actions (This Week)
1. **{action_1}**
   - Priority: High
   - Expected Impact: {impact}
   - Owner: {suggested_owner}
   - Success Metric: {metric}

2. **{action_2}**
   - Priority: High
   - Expected Impact: {impact}
   - Owner: {suggested_owner}
   - Success Metric: {metric}

### Short-term Improvements (This Month)
1. **{improvement_1}**: {description}
2. **{improvement_2}**: {description}
3. **{improvement_3}**: {description}

### Strategic Initiatives (This Quarter)
1. **{initiative_1}**: {description}
2. **{initiative_2}**: {description}

---

## Memory-Based Insights

### Relevant Historical Patterns
From {memory_count} analyzed workflow memories:

1. **Most Successful Approach**: {pattern_description}
   - Used by: {teams/projects}
   - Success rate: {rate}%
   - Key differentiator: {factor}

2. **Common Failure Pattern**: {anti_pattern}
   - Frequency: {frequency}%
   - Impact: {negative_impact}
   - Avoidance strategy: {strategy}

### Learning Opportunities
Based on memory analysis:
- **Skill Gap**: {identified_gap}
- **Process Gap**: {process_improvement}
- **Tool Gap**: {tool_recommendation}

---

## Appendix

### Data Sources
- Workflow tracking data from: {data_source}
- Memory patterns from: {memory_count} historical entries
- Team metrics from: {team_data_source}
- Quality data from: {quality_source}

### Methodology
- Analysis period: {period}
- Confidence intervals: {confidence_method}
- Statistical significance: {significance_level}
- Pattern recognition threshold: {threshold}

### Glossary
- **Efficiency Score**: {definition}
- **Bottleneck**: {definition}
- **Success Pattern**: {definition}
- **Information Loss**: {definition}

---

*Report generated by BMAD Workflow Analytics System v1.0*  
*For questions or customization requests, use `/workflow analytics --help`*