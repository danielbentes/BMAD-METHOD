# Pattern Extraction Rules

## Purpose
Define rules and heuristics for identifying, extracting, and categorizing patterns during brownfield codebase analysis. These rules guide LLMs in recognizing meaningful patterns worth preserving in memory.

## Pattern Identification Criteria

### Minimum Occurrence Threshold
A code structure or approach qualifies as a pattern when:
- **Frequency**: Appears in 3+ distinct locations
- **Consistency**: Implementation varies less than 20%
- **Intentionality**: Shows evidence of deliberate reuse
- **Value**: Provides clear benefit (readability, maintainability, performance)

### Pattern Categories

#### 1. Architectural Patterns
**Identification Rules**:
- Look for consistent separation of concerns
- Check for layer boundaries and interfaces
- Identify communication patterns between components
- Note data flow directions and transformations

**Common Patterns to Detect**:
- MVC/MVP/MVVM variations
- Repository/Service layer patterns
- Event-driven architectures
- Microservices patterns
- API Gateway patterns
- CQRS implementations
- Saga/Orchestration patterns

#### 2. Coding Patterns
**Identification Rules**:
- Analyze recurring code structures
- Look for consistent problem-solving approaches
- Check for design pattern implementations
- Note error handling strategies

**Common Patterns to Detect**:
- Factory patterns (object creation)
- Builder patterns (complex object construction)
- Strategy patterns (algorithm selection)
- Observer patterns (event handling)
- Decorator patterns (behavior extension)
- Singleton usage (with caution flags)
- Dependency injection patterns

#### 3. Testing Patterns
**Identification Rules**:
- Examine test file organization
- Analyze test naming conventions
- Check fixture and mock strategies
- Note assertion patterns

**Common Patterns to Detect**:
- Arrange-Act-Assert structure
- Test data builders
- Mock/stub strategies
- Integration test patterns
- E2E test approaches
- Property-based testing
- Snapshot testing usage

#### 4. Workflow Patterns
**Identification Rules**:
- Analyze git commit patterns
- Check PR/MR structures
- Review CI/CD configurations
- Examine branching strategies

**Common Patterns to Detect**:
- GitFlow variations
- Trunk-based development
- Feature flags usage
- Progressive deployment
- Code review patterns
- Release strategies

## Pattern Extraction Process

### Step 1: Initial Scan
```python
# Pseudo-code for pattern detection
def identify_potential_patterns(codebase):
    patterns = {}
    
    # Scan for structural patterns
    for file in codebase.files:
        structure = extract_structure(file)
        patterns[structure] = patterns.get(structure, 0) + 1
    
    # Filter by frequency threshold
    return {p: count for p, count in patterns.items() if count >= 3}
```

### Step 2: Pattern Validation
Validate identified patterns by checking:
1. **Consistency**: Are implementations similar enough?
2. **Coverage**: What percentage of relevant code follows this pattern?
3. **Evolution**: Has the pattern evolved over time?
4. **Exceptions**: Where is the pattern NOT followed and why?

### Step 3: Pattern Characterization
For each validated pattern, document:
- **Name**: Descriptive identifier
- **Purpose**: What problem it solves
- **Implementation**: How it's typically coded
- **Benefits**: Why it's valuable
- **Variations**: Acceptable deviations
- **Anti-patterns**: What to avoid

## Pattern Quality Scoring

### High-Quality Patterns (Score: 8-10)
- Used consistently across codebase (>80% coverage)
- Clear purpose and benefits
- Well-documented or self-evident
- No significant drawbacks identified
- Team actively maintains pattern

### Medium-Quality Patterns (Score: 5-7)
- Moderate usage (50-80% coverage)
- Benefits outweigh drawbacks
- Some inconsistencies but core idea intact
- May need documentation
- Acceptable for continued use

### Low-Quality Patterns (Score: 1-4)
- Limited usage (<50% coverage)
- Unclear benefits
- Multiple competing approaches exist
- May indicate technical debt
- Consider for refactoring

## Pattern Extraction Rules by Language

### JavaScript/TypeScript
```javascript
// Look for:
// 1. Module patterns
export default class ServiceName {
    constructor(dependency) {
        this.dependency = dependency;
    }
}

// 2. Async patterns
async function fetchData() {
    try {
        const result = await api.call();
        return transform(result);
    } catch (error) {
        logger.error(error);
        throw new CustomError(error);
    }
}

// 3. React patterns
const Component = ({ prop }) => {
    const [state, setState] = useState(initial);
    useEffect(() => {}, [dependency]);
    return <div>{content}</div>;
};
```

### Python
```python
# Look for:
# 1. Class patterns
class Repository:
    def __init__(self, db_connection):
        self._db = db_connection
    
    def find_by_id(self, id: str) -> Optional[Entity]:
        pass

# 2. Decorator patterns
@retry(attempts=3)
@log_execution_time
def process_data(data: List[Dict]) -> Result:
    pass

# 3. Context manager patterns
with database.transaction() as tx:
    tx.execute(query)
    tx.commit()
```

### Java
```java
// Look for:
// 1. Builder patterns
User.builder()
    .name("John")
    .email("john@example.com")
    .build();

// 2. Repository patterns
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
}

// 3. Service patterns
@Service
@Transactional
public class UserService {
    private final UserRepository repository;
}
```

## Pattern Relationship Detection

### Direct Relationships
- **Depends on**: Pattern A requires Pattern B
- **Extends**: Pattern A builds upon Pattern B
- **Conflicts with**: Pattern A incompatible with Pattern B
- **Replaces**: Pattern A supersedes Pattern B

### Indirect Relationships
- **Commonly used with**: Patterns often appear together
- **Alternative to**: Different solution to same problem
- **Precursor to**: Pattern A often evolves into Pattern B

## Anti-Pattern Detection Rules

### Code Smells to Flag
1. **God Objects**: Classes with too many responsibilities
2. **Copy-Paste Programming**: Identical code blocks
3. **Magic Numbers**: Hardcoded values without context
4. **Long Methods**: Functions exceeding 50 lines
5. **Deep Nesting**: More than 4 levels of indentation
6. **Inconsistent Naming**: Mixed conventions

### Architecture Smells to Flag
1. **Circular Dependencies**: A depends on B depends on A
2. **Skip-Level Access**: Layer violations
3. **Distributed Monolith**: Microservices too tightly coupled
4. **Chatty Interfaces**: Excessive inter-service calls
5. **Shared Databases**: Multiple services sharing data store

## Pattern Evolution Tracking

### Version Detection
- Look for comments indicating version (// v2, @deprecated)
- Check git history for pattern introduction
- Note progressive refinements over time
- Document migration patterns (old → new)

### Adoption Tracking
- Count early adopters vs. current usage
- Identify pattern champions (who uses it most)
- Note resistance areas (where pattern not adopted)
- Track success metrics if available

## Output Format for Patterns

### Pattern Memory Structure
```json
{
  "type": "pattern",
  "id": "unique-pattern-identifier",
  "name": "Human-readable pattern name",
  "category": "architectural|coding|testing|workflow",
  "description": "What the pattern does and why",
  "problem_solved": "The specific problem this addresses",
  "implementation": {
    "typical_code": "Example implementation",
    "variations": ["variant1", "variant2"],
    "required_elements": ["element1", "element2"]
  },
  "usage": {
    "frequency": 45,
    "locations": ["path1", "path2"],
    "coverage": "85%",
    "trend": "increasing|stable|decreasing"
  },
  "quality": {
    "score": 8.5,
    "benefits": ["benefit1", "benefit2"],
    "drawbacks": ["drawback1"],
    "maintenance_burden": "low|medium|high"
  },
  "relationships": [
    {
      "pattern_id": "related-pattern",
      "relationship_type": "depends_on|extends|conflicts",
      "strength": 0.8
    }
  ],
  "evolution": {
    "introduced": "2023-01-15",
    "last_modified": "2024-03-20",
    "stability": "stable|evolving|deprecated"
  },
  "team_sentiment": "positive|neutral|negative",
  "recommendations": {
    "action": "maintain|enhance|migrate|deprecate",
    "reasoning": "Why this recommendation"
  }
}
```

## Confidence Scoring Guidelines

### High Confidence (80-100%)
- Pattern appears in majority of relevant contexts
- Clear documentation or comments explain usage
- Consistent implementation across team members
- Git history shows deliberate introduction

### Medium Confidence (60-79%)
- Pattern appears frequently but not universally
- Implementation mostly consistent
- Some variation in approach
- Benefits apparent but not documented

### Low Confidence (40-59%)
- Pattern appears sporadically
- Significant implementation variations
- Unclear if intentional or coincidental
- May be emerging or declining pattern