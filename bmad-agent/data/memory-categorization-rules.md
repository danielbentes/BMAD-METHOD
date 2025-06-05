# Memory Categorization Rules

## Purpose
Define rules and patterns for automatically categorizing memories to ensure consistent organization and efficient retrieval.

## Category Definitions

### 1. Decisions
Memories that capture choices made between alternatives with rationale.

**Identification Patterns**:
- Keywords: "decided", "chose", "selected", "picked", "went with", "opted for"
- Structure: Contains alternatives + rationale + outcome
- Context: Usually includes "because", "due to", "since", "as"

**Auto-Tagging Rules**:
```python
def is_decision_memory(content):
    decision_indicators = [
        "decided to", "chose", "selected", "picked",
        "went with", "opted for", "decision:",
        "vs", "over", "instead of", "rather than"
    ]
    rationale_indicators = [
        "because", "due to", "since", "as", "for",
        "reason:", "rationale:", "why:"
    ]
    
    has_choice = any(indicator in content.lower() for indicator in decision_indicators)
    has_rationale = any(indicator in content.lower() for indicator in rationale_indicators)
    
    return has_choice and has_rationale
```

**Examples**:
- "Decided to use PostgreSQL over MongoDB because we need ACID compliance"
- "Chose microservices architecture due to team scalability requirements"
- "Selected AWS over GCP for better enterprise support"

### 2. Patterns
Recurring approaches or sequences that lead to consistent outcomes.

**Identification Patterns**:
- Keywords: "always", "every time", "pattern", "approach", "method", "strategy"
- Structure: Action + Result + Frequency/Consistency
- Metrics: Success rates, time saved, quality improvements

**Auto-Tagging Rules**:
```python
def is_pattern_memory(content):
    pattern_indicators = [
        "always", "every time", "consistently", "pattern",
        "approach works", "method", "strategy", "technique",
        "reduced by", "improved by", "faster", "better"
    ]
    
    has_pattern = any(indicator in content.lower() for indicator in pattern_indicators)
    has_outcome = bool(re.search(r'\d+%|\d+x|\d+ (hours?|days?|weeks?)', content))
    
    return has_pattern or has_outcome
```

**Examples**:
- "Starting with API design first reduced rework by 70%"
- "Daily standups under 15 minutes improved team productivity"
- "Using feature flags for gradual rollouts prevented 90% of rollback scenarios"

### 3. Mistakes
Negative outcomes that provide learning opportunities.

**Identification Patterns**:
- Keywords: "failed", "mistake", "error", "wrong", "issue", "problem", "bug"
- Structure: What went wrong + Impact + Learning
- Emotions: Frustration, regret, surprise at negative outcome

**Auto-Tagging Rules**:
```python
def is_mistake_memory(content):
    mistake_indicators = [
        "failed", "mistake", "error", "wrong", "broke",
        "bug", "issue", "problem", "crashed", "down",
        "didn't work", "backfired", "caused", "led to"
    ]
    
    negative_impacts = [
        "lost", "wasted", "spent", "cost", "delayed",
        "frustrated", "angry", "disappointed"
    ]
    
    has_mistake = any(indicator in content.lower() for indicator in mistake_indicators)
    has_impact = any(impact in content.lower() for impact in negative_impacts)
    
    return has_mistake and has_impact
```

**Examples**:
- "Skipping tests caused 5 production bugs that took 2 days to fix"
- "Premature optimization wasted a week on unnecessary complexity"
- "Not validating inputs led to SQL injection vulnerability"

### 4. Implementations
Technical implementations and code-specific memories.

**Identification Patterns**:
- Keywords: "implemented", "coded", "built", "developed", "integrated"
- Structure: Technology + Feature + Approach + Outcome
- Technical terms: API names, framework features, code patterns

**Auto-Tagging Rules**:
```python
def is_implementation_memory(content):
    implementation_indicators = [
        "implemented", "coded", "built", "developed",
        "integrated", "deployed", "configured", "setup",
        "using", "with", "framework", "library", "api"
    ]
    
    # Check for code-like patterns
    has_code_pattern = bool(re.search(r'[A-Z][a-z]+[A-Z]|\w+\(\)|\w+\.\w+', content))
    has_implementation = any(indicator in content.lower() for indicator in implementation_indicators)
    
    return has_implementation or has_code_pattern
```

**Examples**:
- "Implemented JWT auth with refresh tokens using jsonwebtoken library"
- "Built real-time notifications with WebSockets and Redis pub/sub"
- "Integrated Stripe payments using webhook pattern for async processing"

### 5. Consultations
Multi-persona or team collaboration outcomes.

**Identification Patterns**:
- Keywords: "consulted", "discussed", "team", "agreed", "consensus", "meeting"
- Structure: Participants + Topic + Perspectives + Outcome
- Multiple viewpoints mentioned

**Auto-Tagging Rules**:
```python
def is_consultation_memory(content):
    consultation_indicators = [
        "consulted", "discussed", "team", "meeting",
        "agreed", "consensus", "decided together",
        "perspectives", "viewpoints", "opinions"
    ]
    
    participant_patterns = [
        r'(?:PM|PO|Dev|QA|Design|Architect)',
        r'(?:team|stakeholder|client|user)',
        r'(?:frontend|backend|fullstack)'
    ]
    
    has_consultation = any(indicator in content.lower() for indicator in consultation_indicators)
    has_participants = any(re.search(pattern, content, re.I) for pattern in participant_patterns)
    
    return has_consultation or has_participants
```

**Examples**:
- "Design review with PM, Architect, and Design resulted in API-first approach"
- "Team consensus: prioritize performance over new features this sprint"
- "Stakeholder meeting decided to delay launch for security audit"

### 6. User Preferences
Personal or team working style preferences.

**Identification Patterns**:
- Keywords: "prefer", "like", "works best", "style", "approach"
- Structure: Preference + Context + Reason
- Personal pronouns: "I", "we", "my", "our"

**Auto-Tagging Rules**:
```python
def is_preference_memory(content):
    preference_indicators = [
        "prefer", "like", "favorite", "works best",
        "style", "i always", "we always", "tend to",
        "better when", "more productive"
    ]
    
    has_preference = any(indicator in content.lower() for indicator in preference_indicators)
    has_personal = bool(re.search(r'\b(I|we|my|our)\b', content, re.I))
    
    return has_preference and has_personal
```

**Examples**:
- "I prefer detailed technical explanations during architecture discussions"
- "Team works best with 2-week sprints instead of 3-week"
- "We're more productive with morning standups at 9:30 AM"

### 7. Quality Metrics
Measurements and quality-related observations.

**Identification Patterns**:
- Keywords: "coverage", "performance", "quality", "metric", "score", "rate"
- Structure: Metric + Value + Context
- Numbers: Percentages, scores, measurements

**Auto-Tagging Rules**:
```python
def is_quality_memory(content):
    quality_indicators = [
        "coverage", "performance", "quality", "metric",
        "score", "rate", "speed", "latency", "uptime",
        "reliability", "maintainability", "security"
    ]
    
    has_quality = any(indicator in content.lower() for indicator in quality_indicators)
    has_metrics = bool(re.search(r'\d+%|\d+ms|\d+s|\d+/\d+', content))
    
    return has_quality and has_metrics
```

**Examples**:
- "Test coverage reached 85% with focus on critical paths"
- "API response time improved from 2.3s to 400ms after caching"
- "Code review caught 12 issues, preventing 3 potential security vulnerabilities"

## Categorization Priority

When content matches multiple categories, apply this priority:
1. **Mistakes** (highest priority - critical learnings)
2. **Decisions** (strategic importance)
3. **Patterns** (reusable knowledge)
4. **Consultations** (team decisions)
5. **Implementations** (technical details)
6. **Quality Metrics** (measurements)
7. **User Preferences** (lowest priority - personal style)

## Automatic Tagging

### Context-Based Tags
```python
def generate_context_tags(content, context):
    tags = []
    
    # Project phase tags
    if context.project_phase:
        tags.append(f"phase:{context.project_phase}")
    
    # Technology tags
    tech_keywords = extract_technologies(content)
    tags.extend([f"tech:{tech}" for tech in tech_keywords])
    
    # Persona tags
    if context.active_persona:
        tags.append(f"persona:{context.active_persona}")
    
    # Time-based tags
    if is_urgent(content):
        tags.append("urgent")
    if is_milestone(content):
        tags.append("milestone")
    
    return tags
```

### Confidence Scoring
```python
def calculate_category_confidence(content, category):
    """Calculate confidence that content belongs to category"""
    
    # Count matching indicators
    indicator_matches = count_category_indicators(content, category)
    
    # Check structure match
    structure_match = check_structure_match(content, category)
    
    # Context relevance
    context_score = assess_context_relevance(content, category)
    
    # Calculate weighted confidence
    confidence = (
        indicator_matches * 0.4 +
        structure_match * 0.3 +
        context_score * 0.3
    )
    
    return min(confidence * 100, 100)
```

## Special Cases

### Mixed Category Content
When content spans multiple categories:
- Split into multiple memories if clearly separable
- Use primary category with secondary category tags
- Maintain relationships between related memories

### Ambiguous Content
When categorization is unclear:
- Default to "general" category
- Add "needs-review" tag
- Request user clarification if confidence < 50%

### Evolution Over Time
- Track categorization accuracy
- Update rules based on user corrections
- Learn new patterns from usage

## Quality Assurance

### Validation Rules
1. Every memory must have exactly one primary category
2. Confidence score must be recorded
3. At least one tag must be applied
4. Timestamp must be accurate
5. Context must be captured

### Review Triggers
- Low confidence categorization (< 60%)
- User corrections to categories
- New patterns emerging
- Category distribution anomalies

## Integration with Other Systems

### Pattern Recognition
- Categories help identify emerging patterns
- Cross-category analysis reveals insights
- Category transitions show evolution

### Search Optimization
- Category-specific search strategies
- Weighted relevance by category
- Category-aware result ranking

### Insight Generation
- Category-specific insight algorithms
- Cross-category correlation analysis
- Predictive categorization for planning