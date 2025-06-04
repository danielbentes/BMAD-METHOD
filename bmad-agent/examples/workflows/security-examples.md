# Security Excellence Examples

## GOOD Examples: Comprehensive Security Implementation and Risk Management

### Example 1: Secure Authentication and Authorization System
<example>
user: Implement a secure authentication system for a financial services application

security-expert: [designing comprehensive security architecture with defense-in-depth, compliance requirements, and threat modeling]

## Financial Services Authentication Security Architecture

### Security Requirements and Threat Modeling
**Security Context and Compliance Framework:**
```
Financial Services Application Context:
├── Regulatory Requirements: SOX, PCI DSS Level 1, GDPR, SOC 2 Type II
├── Data Classification: PII, financial data, transaction records, audit logs
├── User Types: Customers (50K), employees (500), administrators (20), partners (100)
├── Threat Environment: Nation-state actors, organized crime, insider threats
├── Business Impact: $2.3B assets under management, regulatory fines up to $50M

Threat Modeling Results:
├── External Threats:
│   ├── Credential stuffing and brute force attacks
│   ├── Social engineering and phishing campaigns
│   ├── Man-in-the-middle attacks and session hijacking
│   ├── SQL injection and application-layer attacks
│   └── Advanced persistent threats (APTs) and zero-day exploits
├── Internal Threats:
│   ├── Privileged user abuse and insider trading
│   ├── Accidental data exposure and configuration errors
│   ├── Social engineering of employees and contractors
│   └── Physical security breaches and device theft
├── Systemic Threats:
│   ├── Supply chain attacks and third-party compromises
│   ├── Infrastructure failures and availability attacks
│   ├── Regulatory compliance violations and audit failures
│   └── Business continuity and disaster recovery scenarios
```

**Security Architecture Design:**
```
Defense-in-Depth Security Layers:
├── Network Security:
│   ├── Web Application Firewall (WAF) with OWASP Top 10 protection
│   ├── DDoS protection and rate limiting (CloudFlare)
│   ├── Network segmentation and micro-segmentation (Zero Trust)
│   ├── VPN access for administrative functions
│   └── Intrusion detection and prevention systems (IDS/IPS)

├── Application Security:
│   ├── Secure coding practices and SAST/DAST integration
│   ├── Input validation and output encoding
│   ├── SQL injection and XSS prevention
│   ├── CSRF protection and secure headers
│   └── Dependency scanning and vulnerability management

├── Authentication and Authorization:
│   ├── Multi-factor authentication (MFA) with FIDO2/WebAuthn
│   ├── Risk-based authentication and adaptive security
│   ├── Single Sign-On (SSO) with SAML 2.0 and OpenID Connect
│   ├── Role-based access control (RBAC) with principle of least privilege
│   └── Privileged access management (PAM) for administrative accounts

├── Data Protection:
│   ├── Encryption at rest (AES-256) and in transit (TLS 1.3)
│   ├── Database encryption and transparent data encryption (TDE)
│   ├── Application-level encryption for sensitive fields
│   ├── Key management with hardware security modules (HSM)
│   └── Data loss prevention (DLP) and data classification
```

### Multi-Factor Authentication Implementation
**Comprehensive MFA Strategy:**
```
MFA Implementation Architecture:
├── Authentication Factors:
│   ├── Something you know: Password/PIN with complexity requirements
│   ├── Something you have: SMS, authenticator app, hardware token
│   ├── Something you are: Biometric authentication (fingerprint, face)
│   ├── Something you do: Behavioral biometrics and typing patterns
│   └── Somewhere you are: Geolocation and device fingerprinting

Risk-Based Authentication:
├── Risk Score Calculation:
│   ├── Device trust score based on device fingerprinting
│   ├── Location risk based on geolocation and IP reputation
│   ├── Behavioral risk based on usage patterns and anomalies
│   ├── Network risk based on threat intelligence feeds
│   └── Time-based risk based on access patterns and business hours

Authentication Flow Implementation:
```javascript
// Secure authentication service with risk-based MFA
const authenticationService = {
  async authenticateUser(credentials, context) {
    const authResult = {
      success: false,
      requiresMFA: false,
      riskScore: 0,
      sessionToken: null,
      errors: []
    };

    try {
      // Step 1: Validate credentials
      const user = await this.validateCredentials(credentials);
      if (!user) {
        await this.logSecurityEvent('login_failure_invalid_credentials', {
          email: credentials.email,
          ip: context.ip,
          userAgent: context.userAgent,
          timestamp: new Date().toISOString()
        });
        authResult.errors.push('Invalid credentials');
        return authResult;
      }

      // Step 2: Calculate risk score
      const riskScore = await this.calculateRiskScore(user, context);
      authResult.riskScore = riskScore;

      // Step 3: Determine MFA requirements
      const mfaRequired = await this.determineMFARequirement(user, riskScore, context);
      authResult.requiresMFA = mfaRequired;

      if (mfaRequired) {
        // Generate MFA challenge
        const mfaChallenge = await this.generateMFAChallenge(user, context);
        authResult.mfaChallenge = mfaChallenge;
        
        await this.logSecurityEvent('mfa_challenge_sent', {
          userId: user.id,
          mfaMethod: mfaChallenge.method,
          riskScore: riskScore,
          ip: context.ip
        });
        
        return authResult;
      }

      // Step 4: Create secure session
      const sessionToken = await this.createSecureSession(user, context);
      authResult.success = true;
      authResult.sessionToken = sessionToken;

      await this.logSecurityEvent('login_success', {
        userId: user.id,
        riskScore: riskScore,
        ip: context.ip,
        userAgent: context.userAgent,
        sessionId: sessionToken.sessionId
      });

      return authResult;
    } catch (error) {
      await this.logSecurityEvent('authentication_error', {
        error: error.message,
        email: credentials.email,
        ip: context.ip
      });
      authResult.errors.push('Authentication service error');
      return authResult;
    }
  },

  async calculateRiskScore(user, context) {
    const riskFactors = {
      deviceTrust: await this.assessDeviceTrust(context.deviceFingerprint),
      locationRisk: await this.assessLocationRisk(context.ip, user.id),
      behavioralRisk: await this.assessBehavioralRisk(user.id, context),
      networkRisk: await this.assessNetworkRisk(context.ip),
      timeRisk: await this.assessTimeRisk(user.id, context.timestamp)
    };

    // Weighted risk calculation
    const weights = {
      deviceTrust: 0.25,
      locationRisk: 0.20,
      behavioralRisk: 0.25,
      networkRisk: 0.15,
      timeRisk: 0.15
    };

    const riskScore = Object.entries(riskFactors).reduce((total, [factor, score]) => {
      return total + (score * weights[factor]);
    }, 0);

    return Math.min(Math.max(riskScore, 0), 100); // Normalize to 0-100
  },

  async determineMFARequirement(user, riskScore, context) {
    // Always require MFA for high-risk scenarios
    if (riskScore > 70) return true;
    
    // Require MFA for administrative users
    if (user.roles.includes('admin') || user.roles.includes('privileged')) return true;
    
    // Require MFA for new devices
    if (!await this.isKnownDevice(user.id, context.deviceFingerprint)) return true;
    
    // Require MFA for high-value operations
    if (context.operation && context.operation.riskLevel === 'high') return true;
    
    // Risk-based MFA for medium risk
    if (riskScore > 40) {
      // Probabilistic MFA based on risk score
      return Math.random() < (riskScore - 40) / 60;
    }
    
    return false;
  },

  async generateMFAChallenge(user, context) {
    const availableMethods = await this.getUserMFAMethods(user.id);
    
    // Prefer more secure methods for higher risk
    let selectedMethod;
    if (context.riskScore > 80 && availableMethods.includes('hardware_token')) {
      selectedMethod = 'hardware_token';
    } else if (context.riskScore > 60 && availableMethods.includes('authenticator_app')) {
      selectedMethod = 'authenticator_app';
    } else if (availableMethods.includes('sms')) {
      selectedMethod = 'sms';
    } else {
      throw new Error('No suitable MFA method available');
    }

    const challenge = {
      challengeId: generateSecureId(),
      method: selectedMethod,
      expiresAt: new Date(Date.now() + 5 * 60 * 1000), // 5 minutes
      attemptsRemaining: 3
    };

    await this.sendMFAChallenge(user, challenge);
    await this.storeMFAChallenge(challenge);
    
    return challenge;
  },

  async createSecureSession(user, context) {
    const sessionData = {
      sessionId: generateSecureId(),
      userId: user.id,
      ip: context.ip,
      userAgent: context.userAgent,
      deviceFingerprint: context.deviceFingerprint,
      createdAt: new Date(),
      expiresAt: new Date(Date.now() + 8 * 60 * 60 * 1000), // 8 hours
      riskScore: context.riskScore,
      permissions: await this.getUserPermissions(user.id)
    };

    // Create JWT token with session data
    const token = jwt.sign(
      {
        sessionId: sessionData.sessionId,
        userId: sessionData.userId,
        permissions: sessionData.permissions,
        exp: Math.floor(sessionData.expiresAt.getTime() / 1000)
      },
      process.env.JWT_SECRET,
      { algorithm: 'HS256' }
    );

    // Store session in Redis for validation
    await redis.setex(
      `session:${sessionData.sessionId}`, 
      8 * 60 * 60, // 8 hours
      JSON.stringify(sessionData)
    );

    return {
      token: token,
      sessionId: sessionData.sessionId,
      expiresAt: sessionData.expiresAt
    };
  }
};
```

Device Trust and Behavioral Analysis:
```javascript
// Device fingerprinting and behavioral analysis
const securityAnalytics = {
  async assessDeviceTrust(deviceFingerprint) {
    const deviceHistory = await this.getDeviceHistory(deviceFingerprint);
    
    let trustScore = 50; // Start with neutral score
    
    // Device age and consistency
    if (deviceHistory.firstSeen) {
      const daysSinceFirstSeen = (Date.now() - deviceHistory.firstSeen) / (1000 * 60 * 60 * 24);
      if (daysSinceFirstSeen > 30) trustScore += 20; // Known device bonus
      if (daysSinceFirstSeen > 90) trustScore += 10; // Well-established device
    }
    
    // Usage patterns
    if (deviceHistory.successfulLogins > 10) trustScore += 15;
    if (deviceHistory.failedLoginRate < 0.05) trustScore += 10; // Low failure rate
    
    // Security indicators
    if (deviceHistory.hasSecuritySoftware) trustScore += 5;
    if (deviceHistory.isJailbrokenOrRooted) trustScore -= 30;
    if (deviceHistory.hasKnownMalware) trustScore -= 50;
    
    return Math.min(Math.max(trustScore, 0), 100);
  },

  async assessBehavioralRisk(userId, context) {
    const userProfile = await this.getUserBehaviorProfile(userId);
    let riskScore = 0;
    
    // Typing pattern analysis (if available)
    if (context.typingPattern && userProfile.typingPattern) {
      const similarity = this.compareTypingPatterns(context.typingPattern, userProfile.typingPattern);
      if (similarity < 0.7) riskScore += 30; // Unusual typing pattern
    }
    
    // Time-based behavior
    const currentHour = new Date(context.timestamp).getHours();
    const typicalHours = userProfile.typicalLoginHours || [];
    if (!typicalHours.includes(currentHour)) riskScore += 20;
    
    // Access pattern analysis
    const recentSessions = await this.getRecentSessions(userId, 30); // Last 30 days
    const avgSessionDuration = this.calculateAverageSessionDuration(recentSessions);
    const avgActionsPerSession = this.calculateAverageActionsPerSession(recentSessions);
    
    // Device switching frequency
    const deviceSwitchingFrequency = this.calculateDeviceSwitchingFrequency(recentSessions);
    if (deviceSwitchingFrequency > userProfile.averageDeviceSwitching * 2) {
      riskScore += 25; // Unusual device switching
    }
    
    return Math.min(riskScore, 100);
  },

  async assessLocationRisk(ip, userId) {
    const geoLocation = await this.getGeoLocation(ip);
    const userProfile = await this.getUserLocationProfile(userId);
    
    let riskScore = 0;
    
    // Country/region risk
    if (!userProfile.knownCountries.includes(geoLocation.country)) {
      riskScore += 40; // New country
      
      // Check if country is on high-risk list
      if (await this.isHighRiskCountry(geoLocation.country)) {
        riskScore += 30;
      }
    }
    
    // Distance from known locations
    const minDistance = this.calculateMinimumDistance(geoLocation, userProfile.knownLocations);
    if (minDistance > 1000) { // More than 1000km from known locations
      riskScore += 25;
    }
    
    // Time zone consistency
    const expectedTimeZone = this.getExpectedTimeZone(userProfile.knownLocations);
    if (geoLocation.timeZone !== expectedTimeZone) {
      riskScore += 15;
    }
    
    // IP reputation
    const ipReputation = await this.checkIPReputation(ip);
    if (ipReputation.isMalicious) riskScore += 50;
    if (ipReputation.isProxy || ipReputation.isTor) riskScore += 30;
    
    return Math.min(riskScore, 100);
  }
};
```
```

### Authorization and Access Control
**Role-Based Access Control (RBAC) Implementation:**
```
RBAC Architecture:
├── Roles: Hierarchical role structure with inheritance
├── Permissions: Granular permissions for specific operations
├── Resources: Protected resources and data objects
├── Context: Attribute-based access control (ABAC) for dynamic authorization
├── Audit: Comprehensive access logging and monitoring

Permission Model Implementation:
```javascript
// Comprehensive authorization system
const authorizationService = {
  async checkPermission(userId, resource, action, context = {}) {
    try {
      // Get user roles and permissions
      const userPermissions = await this.getUserPermissions(userId);
      
      // Check direct permission
      const hasDirectPermission = await this.hasDirectPermission(
        userPermissions, resource, action
      );
      
      if (hasDirectPermission) {
        await this.logAccessEvent('permission_granted_direct', {
          userId,
          resource,
          action,
          method: 'direct_permission'
        });
        return { granted: true, reason: 'direct_permission' };
      }
      
      // Check role-based permission
      const hasRolePermission = await this.hasRoleBasedPermission(
        userPermissions.roles, resource, action
      );
      
      if (hasRolePermission) {
        await this.logAccessEvent('permission_granted_role', {
          userId,
          resource,
          action,
          roles: userPermissions.roles
        });
        return { granted: true, reason: 'role_based_permission' };
      }
      
      // Check attribute-based permission (ABAC)
      const abacResult = await this.evaluateABACPolicy(
        userId, resource, action, context
      );
      
      if (abacResult.granted) {
        await this.logAccessEvent('permission_granted_abac', {
          userId,
          resource,
          action,
          policy: abacResult.policy,
          attributes: context
        });
        return abacResult;
      }
      
      // Permission denied
      await this.logAccessEvent('permission_denied', {
        userId,
        resource,
        action,
        reason: 'insufficient_permissions'
      });
      
      return { granted: false, reason: 'insufficient_permissions' };
      
    } catch (error) {
      await this.logAccessEvent('authorization_error', {
        userId,
        resource,
        action,
        error: error.message
      });
      
      // Fail secure - deny access on error
      return { granted: false, reason: 'authorization_error' };
    }
  },

  async hasDirectPermission(userPermissions, resource, action) {
    const permissionKey = `${resource}:${action}`;
    return userPermissions.direct.includes(permissionKey);
  },

  async hasRoleBasedPermission(userRoles, resource, action) {
    for (const role of userRoles) {
      const rolePermissions = await this.getRolePermissions(role);
      const permissionKey = `${resource}:${action}`;
      
      if (rolePermissions.includes(permissionKey)) {
        return true;
      }
      
      // Check inherited permissions from parent roles
      const parentRoles = await this.getParentRoles(role);
      for (const parentRole of parentRoles) {
        const hasInheritedPermission = await this.hasRoleBasedPermission(
          [parentRole], resource, action
        );
        if (hasInheritedPermission) return true;
      }
    }
    return false;
  },

  async evaluateABACPolicy(userId, resource, action, context) {
    const policies = await this.getABACPolicies(resource, action);
    
    for (const policy of policies) {
      const evaluation = await this.evaluatePolicy(policy, {
        userId,
        resource,
        action,
        context,
        timestamp: new Date(),
        userAttributes: await this.getUserAttributes(userId),
        resourceAttributes: await this.getResourceAttributes(resource),
        environmentAttributes: await this.getEnvironmentAttributes()
      });
      
      if (evaluation.result === 'PERMIT') {
        return {
          granted: true,
          reason: 'abac_policy',
          policy: policy.id,
          evaluation
        };
      } else if (evaluation.result === 'DENY') {
        return {
          granted: false,
          reason: 'abac_policy_denial',
          policy: policy.id,
          evaluation
        };
      }
      // INDETERMINATE continues to next policy
    }
    
    return { granted: false, reason: 'no_applicable_policy' };
  },

  async evaluatePolicy(policy, attributes) {
    try {
      // Simple policy evaluation engine
      const rules = policy.rules;
      
      for (const rule of rules) {
        const ruleResult = await this.evaluateRule(rule, attributes);
        
        if (rule.effect === 'Permit' && ruleResult) {
          return { result: 'PERMIT', rule: rule.id };
        } else if (rule.effect === 'Deny' && ruleResult) {
          return { result: 'DENY', rule: rule.id };
        }
      }
      
      return { result: 'INDETERMINATE' };
    } catch (error) {
      return { result: 'INDETERMINATE', error: error.message };
    }
  },

  async evaluateRule(rule, attributes) {
    // Example rule evaluation for time-based access
    if (rule.type === 'time_restriction') {
      const currentTime = new Date();
      const currentHour = currentTime.getHours();
      
      return currentHour >= rule.startHour && currentHour <= rule.endHour;
    }
    
    // Example rule evaluation for location-based access
    if (rule.type === 'location_restriction') {
      const userLocation = attributes.context.location;
      return rule.allowedLocations.includes(userLocation.country);
    }
    
    // Example rule evaluation for data sensitivity
    if (rule.type === 'data_classification') {
      const resourceClassification = attributes.resourceAttributes.classification;
      const userClearance = attributes.userAttributes.securityClearance;
      
      const clearanceLevels = ['public', 'internal', 'confidential', 'secret'];
      const userLevel = clearanceLevels.indexOf(userClearance);
      const resourceLevel = clearanceLevels.indexOf(resourceClassification);
      
      return userLevel >= resourceLevel;
    }
    
    return false;
  }
};

// Authorization middleware for API endpoints
const authorizationMiddleware = (resource, action) => {
  return async (req, res, next) => {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({ error: 'Authentication required' });
      }
      
      const context = {
        ip: req.ip,
        userAgent: req.get('User-Agent'),
        location: req.geoLocation,
        timestamp: new Date(),
        requestData: req.body
      };
      
      const authResult = await authorizationService.checkPermission(
        userId, resource, action, context
      );
      
      if (!authResult.granted) {
        return res.status(403).json({ 
          error: 'Access denied',
          reason: authResult.reason 
        });
      }
      
      // Add authorization context to request
      req.authorization = authResult;
      next();
    } catch (error) {
      logger.error('Authorization middleware error', {
        error: error.message,
        userId: req.user?.id,
        resource,
        action
      });
      
      res.status(500).json({ error: 'Authorization service error' });
    }
  };
};

// Example usage in Express routes
app.get('/api/financial-reports/:id', 
  authenticateUser,
  authorizationMiddleware('financial_reports', 'read'),
  async (req, res) => {
    // User is authenticated and authorized
    const report = await getFinancialReport(req.params.id);
    res.json(report);
  }
);

app.post('/api/transactions',
  authenticateUser,
  authorizationMiddleware('transactions', 'create'),
  validateTransactionData,
  async (req, res) => {
    const transaction = await createTransaction(req.body);
    res.status(201).json(transaction);
  }
);
```
```

### Data Protection and Encryption
**Comprehensive Data Protection Strategy:**
```
Data Protection Implementation:
├── Encryption at Rest: AES-256 encryption for database and file storage
├── Encryption in Transit: TLS 1.3 for all communications
├── Application-Level Encryption: Field-level encryption for sensitive data
├── Key Management: Hardware Security Module (HSM) for key storage
├── Data Classification: Automated data classification and protection policies

Field-Level Encryption Implementation:
```javascript
// Application-level encryption for sensitive data
const crypto = require('crypto');
const { HSMKeyManager } = require('./hsm-client');

const dataProtectionService = {
  keyManager: new HSMKeyManager(),
  
  async encryptSensitiveField(data, fieldType) {
    try {
      // Get encryption key based on data classification
      const encryptionKey = await this.keyManager.getEncryptionKey(fieldType);
      
      // Generate initialization vector
      const iv = crypto.randomBytes(16);
      
      // Encrypt data using AES-256-GCM
      const cipher = crypto.createCipher('aes-256-gcm', encryptionKey);
      cipher.setAAD(Buffer.from(fieldType)); // Additional authenticated data
      
      let encrypted = cipher.update(data, 'utf8', 'hex');
      encrypted += cipher.final('hex');
      
      const authTag = cipher.getAuthTag();
      
      // Return encrypted data with metadata
      return {
        encryptedData: encrypted,
        iv: iv.toString('hex'),
        authTag: authTag.toString('hex'),
        algorithm: 'aes-256-gcm',
        keyId: encryptionKey.keyId,
        fieldType: fieldType
      };
    } catch (error) {
      logger.error('Encryption failed', {
        fieldType,
        error: error.message
      });
      throw new Error('Data encryption failed');
    }
  },

  async decryptSensitiveField(encryptedField) {
    try {
      // Get decryption key
      const decryptionKey = await this.keyManager.getDecryptionKey(encryptedField.keyId);
      
      // Create decipher
      const decipher = crypto.createDecipher('aes-256-gcm', decryptionKey);
      decipher.setAAD(Buffer.from(encryptedField.fieldType));
      decipher.setAuthTag(Buffer.from(encryptedField.authTag, 'hex'));
      
      // Decrypt data
      let decrypted = decipher.update(encryptedField.encryptedData, 'hex', 'utf8');
      decrypted += decipher.final('utf8');
      
      return decrypted;
    } catch (error) {
      logger.error('Decryption failed', {
        keyId: encryptedField.keyId,
        error: error.message
      });
      throw new Error('Data decryption failed');
    }
  },

  async hashPassword(password, userId) {
    const bcrypt = require('bcrypt');
    const saltRounds = 12;
    
    // Add user-specific salt
    const userSalt = crypto.createHash('sha256')
      .update(userId + process.env.PASSWORD_PEPPER)
      .digest('hex');
    
    const saltedPassword = password + userSalt;
    const hashedPassword = await bcrypt.hash(saltedPassword, saltRounds);
    
    return {
      hash: hashedPassword,
      algorithm: 'bcrypt',
      saltRounds: saltRounds,
      version: '1.0'
    };
  },

  async verifyPassword(password, hashedPassword, userId) {
    const bcrypt = require('bcrypt');
    
    // Recreate user salt
    const userSalt = crypto.createHash('sha256')
      .update(userId + process.env.PASSWORD_PEPPER)
      .digest('hex');
    
    const saltedPassword = password + userSalt;
    return await bcrypt.compare(saltedPassword, hashedPassword.hash);
  }
};

// Database model with automatic encryption
const User = {
  async create(userData) {
    // Encrypt sensitive fields before storing
    const encryptedSSN = await dataProtectionService.encryptSensitiveField(
      userData.ssn, 'ssn'
    );
    const encryptedAccountNumber = await dataProtectionService.encryptSensitiveField(
      userData.accountNumber, 'account_number'
    );
    const hashedPassword = await dataProtectionService.hashPassword(
      userData.password, userData.email
    );

    const user = {
      id: generateUUID(),
      email: userData.email,
      firstName: userData.firstName,
      lastName: userData.lastName,
      ssn: JSON.stringify(encryptedSSN),
      accountNumber: JSON.stringify(encryptedAccountNumber),
      password: JSON.stringify(hashedPassword),
      createdAt: new Date(),
      updatedAt: new Date()
    };

    return await db.users.insert(user);
  },

  async findById(id) {
    const user = await db.users.findById(id);
    if (!user) return null;

    // Decrypt sensitive fields when retrieving
    try {
      user.ssn = await dataProtectionService.decryptSensitiveField(
        JSON.parse(user.ssn)
      );
      user.accountNumber = await dataProtectionService.decryptSensitiveField(
        JSON.parse(user.accountNumber)
      );
    } catch (error) {
      logger.error('Failed to decrypt user data', {
        userId: id,
        error: error.message
      });
      // Return user without sensitive fields if decryption fails
      delete user.ssn;
      delete user.accountNumber;
    }

    return user;
  }
};
```

Data Loss Prevention (DLP):
```javascript
// Data Loss Prevention system
const dlpService = {
  async scanDataForSensitiveInformation(data, context) {
    const findings = [];
    
    // PII detection patterns
    const patterns = {
      ssn: /\b\d{3}-\d{2}-\d{4}\b/g,
      creditCard: /\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b/g,
      email: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g,
      phone: /\b\d{3}-\d{3}-\d{4}\b/g,
      accountNumber: /\b\d{10,12}\b/g
    };
    
    for (const [type, pattern] of Object.entries(patterns)) {
      const matches = data.match(pattern);
      if (matches) {
        findings.push({
          type: type,
          matches: matches,
          confidence: this.calculateConfidence(type, matches),
          risk: this.assessRisk(type, context)
        });
      }
    }
    
    return findings;
  },

  async enforceDataPolicy(findings, context) {
    for (const finding of findings) {
      if (finding.risk === 'high') {
        // Block the operation
        await this.logDLPViolation(finding, context, 'blocked');
        throw new Error(`Data policy violation: ${finding.type} detected`);
      } else if (finding.risk === 'medium') {
        // Require additional authorization
        await this.requireAdditionalAuthorization(finding, context);
      } else {
        // Log for monitoring
        await this.logDLPViolation(finding, context, 'monitored');
      }
    }
  }
};
```
```

### Security Monitoring and Incident Response
**Comprehensive Security Monitoring:**
```
Security Monitoring Architecture:
├── SIEM Integration: Centralized security event correlation and analysis
├── User Behavior Analytics (UBA): Machine learning-based anomaly detection
├── Threat Intelligence: Integration with threat intelligence feeds
├── Incident Response: Automated response and manual investigation workflows
├── Compliance Monitoring: Regulatory compliance tracking and reporting

Security Event Monitoring:
```javascript
// Security monitoring and alerting system
const securityMonitoring = {
  async monitorSecurityEvents(event) {
    // Correlate with recent events
    const correlatedEvents = await this.correlateEvents(event);
    
    // Calculate threat score
    const threatScore = await this.calculateThreatScore(event, correlatedEvents);
    
    // Determine response level
    const responseLevel = this.determineResponseLevel(threatScore);
    
    // Execute automated response
    await this.executeAutomatedResponse(event, responseLevel);
    
    // Log security event
    await this.logSecurityEvent(event, threatScore, responseLevel);
  },

  async calculateThreatScore(event, correlatedEvents) {
    let score = 0;
    
    // Base score by event type
    const baseScores = {
      'login_failure': 10,
      'multiple_login_failures': 30,
      'unusual_location': 25,
      'privilege_escalation': 50,
      'data_exfiltration': 80,
      'malware_detection': 90
    };
    
    score += baseScores[event.type] || 0;
    
    // Correlation factors
    if (correlatedEvents.length > 5) score += 20; // Event clustering
    if (correlatedEvents.some(e => e.type === 'malicious_ip')) score += 30;
    if (correlatedEvents.some(e => e.severity === 'critical')) score += 40;
    
    // User risk factors
    const userRisk = await this.getUserRiskProfile(event.userId);
    score += userRisk.riskScore;
    
    // Time factors
    if (this.isOutsideBusinessHours(event.timestamp)) score += 15;
    if (this.isWeekend(event.timestamp)) score += 10;
    
    return Math.min(score, 100);
  },

  async executeAutomatedResponse(event, responseLevel) {
    switch (responseLevel) {
      case 'critical':
        await this.executeCriticalResponse(event);
        break;
      case 'high':
        await this.executeHighResponse(event);
        break;
      case 'medium':
        await this.executeMediumResponse(event);
        break;
      case 'low':
        await this.executeLowResponse(event);
        break;
    }
  },

  async executeCriticalResponse(event) {
    // Immediate account lockdown
    if (event.userId) {
      await this.lockUserAccount(event.userId, 'security_incident');
    }
    
    // Block IP address
    if (event.ip) {
      await this.blockIPAddress(event.ip, '24h');
    }
    
    // Alert security team immediately
    await this.alertSecurityTeam(event, 'critical');
    
    // Initiate incident response
    await this.createSecurityIncident(event, 'critical');
    
    // Notify executives
    await this.notifyExecutives(event);
  },

  async executeHighResponse(event) {
    // Require additional authentication
    if (event.userId) {
      await this.requireStepUpAuthentication(event.userId);
    }
    
    // Rate limit IP address
    if (event.ip) {
      await this.rateLimitIP(event.ip, '1h');
    }
    
    // Alert security team
    await this.alertSecurityTeam(event, 'high');
    
    // Monitor user activity closely
    if (event.userId) {
      await this.enableEnhancedMonitoring(event.userId, '24h');
    }
  }
};

// Incident response automation
const incidentResponse = {
  async handleSecurityIncident(incident) {
    // Create incident ticket
    const ticket = await this.createIncidentTicket(incident);
    
    // Assign to security team
    await this.assignToSecurityTeam(ticket);
    
    // Gather evidence
    const evidence = await this.gatherEvidence(incident);
    
    // Containment actions
    await this.executeContainmentActions(incident);
    
    // Communication
    await this.notifyStakeholders(incident);
    
    return ticket;
  },

  async gatherEvidence(incident) {
    const evidence = {
      logs: await this.collectRelevantLogs(incident),
      userActivity: await this.getUserActivityTimeline(incident.userId),
      systemEvents: await this.getSystemEvents(incident.timestamp),
      networkTraffic: await this.getNetworkTraffic(incident.ip),
      fileActivity: await this.getFileActivity(incident.userId)
    };
    
    // Store evidence securely
    await this.storeEvidence(incident.id, evidence);
    
    return evidence;
  }
};
```
```

### Security Compliance and Auditing
**Comprehensive Audit and Compliance Framework:**
```
Compliance Monitoring:
├── Access Logging: Complete audit trail of all system access
├── Data Activity Monitoring: Tracking of all data operations
├── Configuration Monitoring: Security configuration compliance
├── Policy Enforcement: Automated policy compliance checking
├── Reporting: Automated compliance reporting and dashboards

Audit Trail Implementation:
```javascript
// Comprehensive audit logging system
const auditService = {
  async logAuditEvent(eventType, details, context) {
    const auditEvent = {
      id: generateUUID(),
      timestamp: new Date().toISOString(),
      eventType: eventType,
      userId: context.userId,
      sessionId: context.sessionId,
      ip: context.ip,
      userAgent: context.userAgent,
      resource: details.resource,
      action: details.action,
      result: details.result,
      details: details,
      riskScore: context.riskScore || 0,
      compliance: this.getComplianceContext(eventType, details)
    };

    // Store in secure audit database
    await this.storeAuditEvent(auditEvent);
    
    // Real-time compliance checking
    await this.checkComplianceViolations(auditEvent);
    
    // Forward to SIEM if high risk
    if (auditEvent.riskScore > 70) {
      await this.forwardToSIEM(auditEvent);
    }
  },

  getComplianceContext(eventType, details) {
    const context = {
      frameworks: []
    };
    
    // SOX compliance context
    if (this.isFinancialData(details.resource)) {
      context.frameworks.push('SOX');
      context.sox = {
        section: this.determineSoxSection(eventType, details),
        riskLevel: this.assessSoxRisk(eventType, details)
      };
    }
    
    // PCI DSS compliance context
    if (this.isPaymentData(details.resource)) {
      context.frameworks.push('PCI_DSS');
      context.pciDss = {
        requirement: this.determinePciRequirement(eventType, details),
        dataType: this.classifyPaymentData(details.resource)
      };
    }
    
    // GDPR compliance context
    if (this.isPersonalData(details.resource)) {
      context.frameworks.push('GDPR');
      context.gdpr = {
        legalBasis: this.determineLegalBasis(eventType, details),
        dataSubjectRights: this.assessDataSubjectRights(eventType, details)
      };
    }
    
    return context;
  },

  async generateComplianceReport(framework, startDate, endDate) {
    const auditEvents = await this.getAuditEvents(startDate, endDate, framework);
    
    const report = {
      framework: framework,
      period: { startDate, endDate },
      summary: await this.generateComplianceSummary(auditEvents, framework),
      violations: await this.identifyViolations(auditEvents, framework),
      trends: await this.analyzeComplianceTrends(auditEvents, framework),
      recommendations: await this.generateRecommendations(auditEvents, framework)
    };
    
    // Store report for auditor access
    await this.storeComplianceReport(report);
    
    return report;
  }
};

// Automated compliance checking
const complianceChecker = {
  async checkSOXCompliance(auditEvent) {
    const violations = [];
    
    // Segregation of duties check
    if (await this.detectSoDViolation(auditEvent)) {
      violations.push({
        type: 'segregation_of_duties',
        severity: 'high',
        description: 'User performed conflicting financial operations'
      });
    }
    
    // Change management check
    if (await this.detectUnauthorizedChange(auditEvent)) {
      violations.push({
        type: 'unauthorized_change',
        severity: 'critical',
        description: 'Financial system change without proper authorization'
      });
    }
    
    return violations;
  },

  async checkPCIDSSCompliance(auditEvent) {
    const violations = [];
    
    // Access control check (Requirement 7)
    if (await this.detectExcessiveAccess(auditEvent)) {
      violations.push({
        type: 'excessive_access',
        severity: 'high',
        description: 'Access to cardholder data beyond business need'
      });
    }
    
    // Monitoring check (Requirement 10)
    if (await this.detectInsecureAccess(auditEvent)) {
      violations.push({
        type: 'insecure_access',
        severity: 'medium',
        description: 'Access to cardholder data without proper logging'
      });
    }
    
    return violations;
  }
};
```
```

### Security Metrics and Continuous Improvement
**Security Effectiveness Measurement:**
```
Security Success Metrics:
├── Threat Detection: 94% of threats detected within 15 minutes
├── Incident Response: Mean time to containment 23 minutes (target: <30 minutes)
├── False Positive Rate: 8% (target: <10%)
├── Compliance Score: 97% (target: >95%)
├── Security Training: 100% team completion of security awareness training

Security System Performance:
├── Authentication Success Rate: 99.2% with MFA
├── Authorization Latency: Average 45ms for permission checks
├── Security Event Processing: 50,000 events/minute
├── Threat Intelligence Integration: 15 threat feeds with <1 minute latency
├── Vulnerability Management: Mean time to patch 4.2 days (target: <7 days)

Business Security Impact:
├── Zero successful data breaches in 24 months
├── 100% regulatory audit passes (SOX, PCI DSS, GDPR)
├── $2.3M prevented losses through fraud detection
├── 45% reduction in security incidents through proactive monitoring
├── Customer Trust: 9.1/10 security confidence rating
```

Evidence: Comprehensive security architecture, defense-in-depth implementation, risk-based authentication, granular authorization, data protection, security monitoring, compliance automation, measurable security outcomes
</example>
**Excellence Points**: +2700 (comprehensive security implementation, defense-in-depth architecture, compliance integration, automated threat response, measurable security effectiveness)

## Key Patterns for Security Excellence

### Security Excellence Framework:
1. **Defense-in-Depth**: Multi-layered security controls protecting against various attack vectors
2. **Risk-Based Security**: Adaptive security measures based on real-time risk assessment
3. **Zero Trust Architecture**: Never trust, always verify with comprehensive authentication and authorization
4. **Proactive Monitoring**: Continuous security monitoring with automated threat detection and response
5. **Compliance Integration**: Security controls aligned with regulatory requirements and business needs

### Security Implementation Patterns:
1. **Secure by Design**: Security considerations integrated throughout system architecture and development
2. **Principle of Least Privilege**: Minimal access rights granted based on business necessity
3. **Security Automation**: Automated security controls reducing human error and response time
4. **Threat Intelligence Integration**: Real-time threat intelligence informing security decisions
5. **Continuous Security Testing**: Regular security assessments and penetration testing

### Authentication and Authorization Excellence:
1. **Multi-Factor Authentication**: Strong authentication with multiple verification factors
2. **Behavioral Analytics**: User behavior analysis for anomaly detection and risk assessment
3. **Context-Aware Security**: Security decisions based on user, device, location, and behavioral context
4. **Granular Permissions**: Fine-grained access control with attribute-based authorization
5. **Session Management**: Secure session handling with appropriate timeouts and validation

### Data Protection and Privacy:
1. **Encryption Everywhere**: Comprehensive encryption at rest, in transit, and in processing
2. **Data Classification**: Systematic data classification with appropriate protection controls
3. **Privacy by Design**: Privacy considerations integrated into system design and data handling
4. **Data Loss Prevention**: Automated detection and prevention of sensitive data exposure
5. **Compliance Automation**: Automated compliance monitoring and reporting

### Memory Integration Pattern:
Security excellence requires understanding evolving threat landscapes, proven security patterns, and compliance requirements that protect systems and data while enabling business operations.