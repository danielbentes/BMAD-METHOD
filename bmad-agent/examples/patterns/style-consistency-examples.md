# Style Consistency Examples

## Overview
Real-world examples demonstrating how BMAD agent personas automatically discover, apply, and enforce coding style consistency across different programming languages and project types.

## Example 1: TypeScript React Project - Automatic Style Discovery

### Scenario
Dev persona working on a mature React TypeScript project needs to add a new user management component.

### Style Discovery Process

**Memory Bootstrap Phase**:
```typescript
// Existing codebase patterns discovered
src/
  components/
    user-list.component.tsx      // Pattern: kebab-case with .component
    user-profile.component.tsx   // Pattern: feature-based naming
  services/
    userService.ts              // Pattern: camelCase services
    apiClient.ts                // Pattern: descriptive service names
```

**Discovered Style Rules**:
```json
{
  "type": "coding-style",
  "language": "typescript",
  "style_category": "naming-conventions",
  "rules": {
    "components": "kebab-case-with-component-suffix",
    "services": "camelCase-with-Service-suffix",
    "interfaces": "PascalCase-with-I-prefix",
    "props": "camelCase-descriptive"
  },
  "confidence": 0.95
}
```

### Style Application Example

**Before Style Application (Generic)**:
```typescript
// User creates component without style awareness
import React from 'react';

interface Props {
  data: any;
  onChange: Function;
}

export default function UserManager(props: Props) {
  const handleClick = () => {
    console.log('Processing...');
  };
  
  return <div>User Manager</div>;
}
```

**After Automatic Style Application**:
```typescript
// Dev persona automatically applies discovered patterns
import React from 'react';
import { logger } from '../utils/logger';

interface IUserManagerProps {
  userData: UserData;
  onUserUpdate: (user: UserData) => void;
}

export const UserManagerComponent: React.FC<IUserManagerProps> = ({
  userData,
  onUserUpdate
}) => {
  const handleUserUpdate = (updatedUser: UserData): void => {
    logger.info('Processing user update', { userId: updatedUser.id });
    onUserUpdate(updatedUser);
  };
  
  return (
    <div className="user-manager">
      {/* Component implementation */}
    </div>
  );
};
```

**Style Consistency Analysis**:
```xml
<style_analysis>
  <applied_patterns>
    <component_naming>kebab-case UserManagerComponent follows project pattern</component_naming>
    <interface_naming>IUserManagerProps matches I-prefix convention</interface_naming>
    <prop_naming>userData, onUserUpdate follow camelCase descriptive pattern</prop_naming>
    <logging>logger.info matches project logging pattern instead of console.log</logging>
  </applied_patterns>
  <consistency_score>98%</consistency_score>
  <patterns_referenced>user-list.component.tsx, userService.ts patterns</patterns_referenced>
</style_analysis>
```

## Example 2: Python Django Project - Cross-Language Consistency

### Scenario
Dev persona working on a Django backend needs to add API endpoints while maintaining Python conventions.

### Discovered Python Patterns
```python
# Existing codebase analysis results
# File: users/models.py
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

# File: users/serializers.py  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# File: users/views.py
def list_users(request):
    users = User.objects.all()
    return JsonResponse({'users': list(users.values())})
```

**Extracted Style Memory**:
```json
{
  "type": "coding-style",
  "language": "python",
  "style_category": "django-patterns",
  "rules": {
    "model_naming": "singular-PascalCase",
    "field_naming": "snake_case",
    "view_functions": "verb_noun_pattern",
    "class_organization": "fields-then-meta-then-methods",
    "imports": "django-first-then-third-party-then-local"
  },
  "confidence": 0.92
}
```

### Style-Consistent Implementation

**Task**: Add organization management endpoints

**Implementation with Style Consistency**:
```python
# organizations/models.py - Following discovered patterns
from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):  # Singular PascalCase
    organization_name = models.CharField(max_length=200)  # snake_case
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:  # Meta after fields, following pattern
        db_table = 'organizations'
        ordering = ['-created_at']
    
    def __str__(self):  # Methods after Meta
        return self.organization_name

# organizations/serializers.py - Following discovered patterns
from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'organization_name', 'description', 'created_at']

# organizations/views.py - Following discovered patterns
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Organization
from .serializers import OrganizationSerializer

def list_organizations(request):  # verb_noun pattern
    """Retrieve all organizations."""
    organizations = Organization.objects.all()
    serializer = OrganizationSerializer(organizations, many=True)
    return JsonResponse({'organizations': serializer.data})

@require_http_methods(["POST"])
def create_organization(request):  # verb_noun pattern
    """Create a new organization."""
    serializer = OrganizationSerializer(data=request.POST)
    if serializer.is_valid():
        organization = serializer.save()
        return JsonResponse(
            {'organization': OrganizationSerializer(organization).data}, 
            status=201
        )
    return JsonResponse({'errors': serializer.errors}, status=400)
```

**Style Validation Check**:
```xml
<style_analysis>
  <patterns_matched>
    <model_naming>Organization follows singular PascalCase pattern</model_naming>
    <field_naming>organization_name, created_at follow snake_case pattern</field_naming>
    <view_naming>list_organizations, create_organization follow verb_noun pattern</view_naming>
    <class_structure>fields-Meta-methods order maintained</class_structure>
  </patterns_matched>
  <consistency_score>96%</consistency_score>
  <memory_patterns_used>users/models.py, users/views.py patterns</memory_patterns_used>
</style_analysis>
```

## Example 3: Java Spring Boot - Enterprise Style Compliance

### Scenario
Architect persona designing microservice architecture discovers existing style patterns for new service implementation.

### Enterprise Java Patterns Discovered
```java
// Existing service patterns
@Service
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;
    
    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }
    
    public UserDto createUser(CreateUserRequest request) {
        validateUserRequest(request);
        
        User user = User.builder()
            .username(request.getUsername())
            .email(request.getEmail())
            .build();
            
        User savedUser = userRepository.save(user);
        emailService.sendWelcomeEmail(savedUser.getEmail());
        
        return UserDto.from(savedUser);
    }
    
    private void validateUserRequest(CreateUserRequest request) {
        if (StringUtils.isBlank(request.getUsername())) {
            throw new ValidationException("Username is required");
        }
    }
}
```

**Style Memory Created**:
```json
{
  "type": "coding-style",
  "language": "java",
  "style_category": "spring-boot-enterprise",
  "rules": {
    "class_naming": "PascalCase-with-type-suffix",
    "method_naming": "camelCase-verb-phrases",
    "field_naming": "camelCase-final-for-dependencies",
    "constructor_injection": "preferred-over-field-injection",
    "method_organization": "public-then-private",
    "builder_pattern": "preferred-for-entity-creation",
    "exception_handling": "specific-exceptions-with-messages"
  },
  "confidence": 0.94
}
```

### Consistent New Service Implementation

**Task**: Implement OrderService following discovered patterns

```java
// OrderService.java - Automatically styled to match existing patterns
package com.company.orders.service;

import com.company.orders.dto.OrderDto;
import com.company.orders.dto.CreateOrderRequest;
import com.company.orders.entity.Order;
import com.company.orders.repository.OrderRepository;
import com.company.orders.service.PaymentService;
import com.company.orders.service.InventoryService;
import com.company.orders.exception.ValidationException;
import com.company.orders.exception.InsufficientInventoryException;

import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Service  // Following discovered annotation pattern
@RequiredArgsConstructor  // Following constructor injection pattern
@Slf4j  // Following logging pattern
public class OrderService {  // PascalCase with Service suffix
    
    private final OrderRepository orderRepository;  // final fields for dependencies
    private final PaymentService paymentService;
    private final InventoryService inventoryService;
    
    public OrderDto createOrder(CreateOrderRequest request) {  // public methods first
        log.info("Creating order for user: {}", request.getUserId());
        
        validateOrderRequest(request);  // validation method call pattern
        checkInventoryAvailability(request);
        
        Order order = Order.builder()  // builder pattern usage
            .userId(request.getUserId())
            .productId(request.getProductId())
            .quantity(request.getQuantity())
            .totalAmount(calculateTotalAmount(request))
            .build();
            
        Order savedOrder = orderRepository.save(order);
        paymentService.processPayment(savedOrder.getTotalAmount(), request.getPaymentDetails());
        
        log.info("Order created successfully: {}", savedOrder.getId());
        return OrderDto.from(savedOrder);  // DTO conversion pattern
    }
    
    public OrderDto getOrder(Long orderId) {  // camelCase verb phrases
        Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> new OrderNotFoundException("Order not found: " + orderId));
        return OrderDto.from(order);
    }
    
    private void validateOrderRequest(CreateOrderRequest request) {  // private methods last
        if (request.getUserId() == null) {
            throw new ValidationException("User ID is required");  // specific exceptions
        }
        if (request.getQuantity() <= 0) {
            throw new ValidationException("Quantity must be greater than zero");
        }
    }
    
    private void checkInventoryAvailability(CreateOrderRequest request) {
        if (!inventoryService.isAvailable(request.getProductId(), request.getQuantity())) {
            throw new InsufficientInventoryException(
                "Insufficient inventory for product: " + request.getProductId()
            );
        }
    }
    
    private BigDecimal calculateTotalAmount(CreateOrderRequest request) {
        Product product = inventoryService.getProduct(request.getProductId());
        return product.getPrice().multiply(BigDecimal.valueOf(request.getQuantity()));
    }
}
```

**Pattern Compliance Check**:
```xml
<style_analysis>
  <enterprise_patterns_applied>
    <naming>OrderService follows PascalCase-Service pattern</naming>
    <dependency_injection>Constructor injection with @RequiredArgsConstructor</dependency_injection>
    <method_organization>public createOrder, getOrder before private methods</method_organization>
    <builder_usage>Order.builder() follows discovered entity creation pattern</builder_usage>
    <exception_handling>Specific ValidationException and InsufficientInventoryException</exception_handling>
    <logging>slf4j with structured logging messages</logging>
  </enterprise_patterns_applied>
  <consistency_score>97%</consistency_score>
  <patterns_source>UserService.java enterprise patterns</patterns_source>
</style_analysis>
```

## Example 4: Cross-Language Project Style Coordination

### Scenario
Full-stack application with React frontend and Node.js backend requiring style consistency across both layers.

### Frontend Patterns (TypeScript React)
```typescript
// components/user-dashboard.component.tsx
export interface IUserDashboardProps {
  userId: string;
  onUserUpdate: (user: UserData) => void;
}

export const UserDashboardComponent: React.FC<IUserDashboardProps> = ({
  userId,
  onUserUpdate
}) => {
  const [userData, setUserData] = useState<UserData | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  
  const handleUserDataFetch = async (): Promise<void> => {
    setIsLoading(true);
    try {
      const user = await userService.getUserById(userId);
      setUserData(user);
    } catch (error) {
      logger.error('Failed to fetch user data', { error, userId });
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <div className="user-dashboard">
      {/* Component JSX */}
    </div>
  );
};
```

### Backend Patterns (Node.js Express)
```javascript
// routes/user.routes.js
const express = require('express');
const { userController } = require('../controllers');
const { authMiddleware, validationMiddleware } = require('../middleware');

const router = express.Router();

router.get('/users/:userId', 
  authMiddleware.verifyToken,
  validationMiddleware.validateUserId,
  userController.getUserById
);

router.put('/users/:userId',
  authMiddleware.verifyToken,
  validationMiddleware.validateUserUpdate,
  userController.updateUser
);

module.exports = router;

// controllers/user.controller.js
const { userService } = require('../services');
const { logger } = require('../utils');

const getUserById = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const userData = await userService.findUserById(userId);
    
    if (!userData) {
      return res.status(404).json({
        error: 'User not found',
        userId
      });
    }
    
    logger.info('User data retrieved successfully', { userId });
    res.json({ userData });
  } catch (error) {
    logger.error('Failed to retrieve user data', { error, userId: req.params.userId });
    next(error);
  }
};

module.exports = {
  getUserById,
  updateUser
};
```

### Cross-Language Style Memory
```json
{
  "type": "coding-style",
  "language": "multi-language",
  "style_category": "full-stack-consistency",
  "rules": {
    "error_handling": "try-catch-with-structured-logging",
    "async_patterns": "async-await-preferred-over-promises",
    "naming_alignment": "camelCase-for-variables-and-functions",
    "logging_consistency": "structured-logging-with-context",
    "api_patterns": "RESTful-with-descriptive-endpoints",
    "data_flow": "service-layer-for-business-logic"
  },
  "cross_language_patterns": {
    "frontend_backend_alignment": "matching-service-method-names",
    "error_handling_consistency": "same-error-structure-format",
    "logging_correlation": "shared-correlation-id-patterns"
  }
}
```

### Style-Consistent API Implementation

**Task**: Add organization management to both frontend and backend

**Backend Implementation**:
```javascript
// routes/organization.routes.js - Following established patterns
const express = require('express');
const { organizationController } = require('../controllers');
const { authMiddleware, validationMiddleware } = require('../middleware');

const router = express.Router();

router.get('/organizations/:organizationId',  // Follows user.routes.js pattern
  authMiddleware.verifyToken,
  validationMiddleware.validateOrganizationId,
  organizationController.getOrganizationById
);

// controllers/organization.controller.js - Following user.controller.js pattern
const { organizationService } = require('../services');
const { logger } = require('../utils');

const getOrganizationById = async (req, res, next) => {  // Matches getUserById pattern
  try {
    const { organizationId } = req.params;
    const organizationData = await organizationService.findOrganizationById(organizationId);
    
    if (!organizationData) {  // Same error handling pattern
      return res.status(404).json({
        error: 'Organization not found',
        organizationId
      });
    }
    
    logger.info('Organization data retrieved successfully', { organizationId });  // Same logging pattern
    res.json({ organizationData });  // Same response structure
  } catch (error) {
    logger.error('Failed to retrieve organization data', { 
      error, 
      organizationId: req.params.organizationId 
    });
    next(error);
  }
};
```

**Frontend Implementation**:
```typescript
// components/organization-dashboard.component.tsx - Following user-dashboard pattern
export interface IOrganizationDashboardProps {  // Same interface naming pattern
  organizationId: string;
  onOrganizationUpdate: (org: OrganizationData) => void;
}

export const OrganizationDashboardComponent: React.FC<IOrganizationDashboardProps> = ({
  organizationId,
  onOrganizationUpdate
}) => {
  const [organizationData, setOrganizationData] = useState<OrganizationData | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  
  const handleOrganizationDataFetch = async (): Promise<void> => {  // Same async pattern
    setIsLoading(true);
    try {
      const organization = await organizationService.getOrganizationById(organizationId);
      setOrganizationData(organization);
    } catch (error) {
      logger.error('Failed to fetch organization data', { error, organizationId });  // Same error logging
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <div className="organization-dashboard">  {/* Same CSS class pattern */}
      {/* Component JSX */}
    </div>
  );
};
```

**Cross-Language Consistency Analysis**:
```xml
<style_analysis>
  <cross_language_consistency>
    <naming_patterns>
      <frontend>getUserById, handleUserDataFetch</frontend>
      <backend>getUserById, findUserById</backend>
      <alignment>98% - consistent verb-noun patterns</alignment>
    </naming_patterns>
    <error_handling>
      <frontend>try-catch with structured logging</frontend>
      <backend>try-catch with same logging structure</backend>
      <consistency>100% - identical error handling approach</consistency>
    </error_handling>
    <async_patterns>
      <both_layers>async-await preferred over promises</both_layers>
      <consistency>100% - no promise chains found</consistency>
    </async_patterns>
  </cross_language_consistency>
  <overall_consistency_score>97%</overall_consistency_score>
</style_analysis>
```

## Example 5: Style Conflict Resolution

### Scenario
Dev persona encounters conflicting style patterns in legacy codebase during refactoring.

### Conflicting Patterns Detected
```typescript
// Legacy pattern A (40% of files)
class UserManager {
    private _users: User[] = [];
    
    public addUser(user: User): void {
        this._users.push(user);
    }
}

// Legacy pattern B (35% of files)  
class UserService {
    private users: User[] = [];
    
    addUser(user: User): void {
        this.users.push(user);
    }
}

// Modern pattern C (25% of files)
export class UserService {
    private readonly users: User[] = [];
    
    public addUser(user: User): void {
        this.users.push(user);
    }
}
```

### Style Conflict Analysis
```json
{
  "type": "style-conflict-analysis",
  "language": "typescript",
  "conflicts": [
    {
      "category": "private_member_naming",
      "patterns": [
        {"pattern": "underscore_prefix", "usage": 0.40, "files": 23},
        {"pattern": "no_prefix", "usage": 0.35, "files": 20},
        {"pattern": "readonly_modifier", "usage": 0.25, "files": 14}
      ],
      "recommendation": "standardize_on_readonly_modifier",
      "rationale": "Modern TypeScript best practice, more explicit"
    },
    {
      "category": "method_visibility",
      "patterns": [
        {"pattern": "explicit_public", "usage": 0.65, "files": 37},
        {"pattern": "implicit_public", "usage": 0.35, "files": 20}
      ],
      "recommendation": "explicit_public_keywords",
      "rationale": "Better clarity and consistency with private keywords"
    }
  ]
}
```

### Resolution Strategy Implementation
```typescript
// Dev persona applies conflict resolution strategy
<decision_analysis>
  <conflict_context>
    <legacy_patterns>Three competing approaches to class member access</legacy_patterns>
    <team_preference>Modern TypeScript practices preferred based on recent files</team_preference>
    <migration_effort>Low - automated refactoring possible</migration_effort>
  </conflict_context>
  
  <resolution_options>
    <option_1>
      <approach>Keep existing patterns as-is</approach>
      <pros>No migration effort</pros>
      <cons>Continued inconsistency, confusing for new developers</cons>
    </option_1>
    
    <option_2>
      <approach>Gradual migration to modern pattern</approach>
      <pros>Consistent improvement, minimal disruption</pros>
      <cons>Temporary mixed state</cons>
    </option_2>
    
    <option_3>
      <approach>Full codebase modernization</approach>
      <pros>Complete consistency immediately</pros>
      <cons>Large changeset, potential merge conflicts</cons>
    </option_3>
  </resolution_options>
  
  <recommendation>
    <chosen_approach>option_2</chosen_approach>
    <rationale>Balances consistency improvement with practical concerns</rationale>
    <implementation>Modernize new code, gradually refactor touched legacy code</implementation>
  </recommendation>
</decision_analysis>

// Implementation following resolution strategy
export class OrganizationService {  // Modern pattern for new code
    private readonly organizations: Organization[] = [];
    private readonly logger = createLogger('OrganizationService');
    
    public addOrganization(organization: Organization): void {
        this.validateOrganization(organization);
        this.organizations.push(organization);
        this.logger.info('Organization added', { id: organization.id });
    }
    
    public findOrganizationById(id: string): Organization | undefined {
        return this.organizations.find(org => org.id === id);
    }
    
    private validateOrganization(organization: Organization): void {
        if (!organization.name) {
            throw new ValidationError('Organization name is required');
        }
    }
}
```

### Memory Update for Resolved Style
```json
{
  "type": "coding-style",
  "language": "typescript",
  "style_category": "class-member-patterns",
  "rules": {
    "private_members": "readonly-modifier-preferred",
    "method_visibility": "explicit-public-keywords",
    "member_naming": "descriptive-camelCase-no-underscore",
    "class_organization": "readonly-fields-public-methods-private-methods"
  },
  "migration_strategy": {
    "approach": "gradual-modernization",
    "new_code": "always-modern-pattern",
    "legacy_code": "modernize-when-touched",
    "conflict_resolution": "modern-typescript-practices-preferred"
  },
  "confidence": 0.88,
  "evidence": "analysis-of-57-class-files-with-trend-toward-modern-patterns"
}
```

## Key Benefits Demonstrated

### 1. **Automatic Pattern Discovery**
- No manual style guide creation needed
- Patterns extracted from actual codebase usage
- High-confidence rules based on statistical analysis

### 2. **Consistent Code Generation**
- All new code follows discovered patterns automatically
- Cross-file consistency maintained
- Reduces cognitive load in code reviews

### 3. **Intelligent Conflict Resolution**
- Competing patterns analyzed and resolved systematically
- Migration strategies based on practical considerations
- Gradual improvement without disrupting workflow

### 4. **Cross-Language Coordination**
- Full-stack projects maintain consistency across technologies
- API naming patterns aligned between frontend and backend
- Error handling and logging approaches synchronized

### 5. **Memory-Enhanced Learning**
- Style decisions stored for future reference
- Pattern confidence improves over time
- Project-specific conventions preserved and applied

These examples demonstrate how the BMAD Method's coding style consistency approach transforms ad-hoc style decisions into systematic, memory-enhanced pattern application that scales across languages, team members, and project complexity.