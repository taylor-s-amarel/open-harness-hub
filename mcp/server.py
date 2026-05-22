"""Open Harness Hub — MCP server stub (auto-generated).

Run:
  pip install mcp
  python server.py

This stub exposes every tool/* manifest from the hub plus model-callable
processors. Implement the body of each `_run_<name>(args)` function with the
real backend (HTTP call, Python callable, etc.) — the schema validation and
JSON-RPC plumbing are handled by the SDK.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

# ── Tool definitions (auto-generated, do not edit) ─────────────────────────

TOOLS: list[dict] = [
    {
        "name": "json-schema-validator",
        "title": "JSON Schema 2020-12 validator",
        "description": "Validates a candidate JSON object against a JSON Schema 2020-12\ndocument. Used by `processor/verify-tool-validate-criterion` to\nenforce structural acceptance bars on pipeline outputs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {
                    "description": "Candidate JSON value to validate."
                },
                "schema_path": {
                    "type": "string",
                    "description": "Path to schema file relative to repo root."
                }
            },
            "required": [
                "target",
                "schema_path"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "pass": {
                    "type": "boolean"
                },
                "errors": {
                    "type": "array",
                    "items": {
                        "type": "object"
                    }
                },
                "error_count": {
                    "type": "integer"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/json-schema-validator",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "cbp-wro-lookup",
        "title": "US CBP Withhold Release Order + UFLPA Entity List lookup",
        "description": "Check a supplier name + geography against:\n - US CBP Withhold Release Orders (active)\n - US CBP Findings list (escalated WROs that became confirmed\n   forced-labor determinations)\n - US UFLPA Entity List (Xinjiang-region production and high-\n   priority sector entities; goods presumed inadmissible under\n   19 USC \u00a71307)\n\nReturns matches with the order ID, date, target commodity, target\ngeography, and current status. A hit on any list HALTS the routine\ngrading flow per the lead company's US-customs counsel protocol\n(see `persona/esg-auditor` hard rule).\n\nImplementation pulls from the offline snapshot in\n`knowledge-pack/high-risk-corridors-and-sectors` (data/cbp-wro-\nactive-snapshot.jsonl + data/uflpa-entity-list-snapshot.jsonl).\nFor live checks, the implementation can scrape cbp.gov directly\n(rate-limited) or use a paid data vendor; both kept out of the\ndefault callable to avoid surprise egress.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "supplier_name": {
                    "type": "string"
                },
                "supplier_country": {
                    "type": "string",
                    "description": "ISO 3166-1 alpha-2."
                },
                "commodity_codes": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional HS code(s) of products in scope."
                },
                "threshold": {
                    "type": "number",
                    "default": 0.9,
                    "description": "Jaro-Winkler fuzz threshold."
                },
                "lists": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "wro_active",
                            "wro_findings",
                            "uflpa_entity_list"
                        ]
                    }
                }
            },
            "required": [
                "supplier_name",
                "lists"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "matches": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "order_id": {
                                "type": "string"
                            },
                            "source_list": {
                                "type": "string"
                            },
                            "target_entity": {
                                "type": "string"
                            },
                            "target_geography": {
                                "type": "string"
                            },
                            "target_commodity": {
                                "type": "string"
                            },
                            "issued_on": {
                                "type": "string",
                                "format": "date"
                            },
                            "status": {
                                "type": "string",
                                "enum": [
                                    "active",
                                    "modified",
                                    "revoked",
                                    "finding"
                                ]
                            },
                            "score": {
                                "type": "number"
                            }
                        }
                    }
                },
                "snapshot_date": {
                    "type": "string",
                    "format": "date"
                },
                "halt_recommended": {
                    "type": "boolean"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/cbp-wro-lookup",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "esg",
                "supply_chain",
                "compliance"
            ],
            "ohh:capability": [
                "verification",
                "safety_gating"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "sanctions-check",
        "title": "Sanctions list check",
        "description": "Check a normalized entity name against one or more sanctions lists\n(OFAC SDN, UN Consolidated, EU Consolidated, HMT, or institutional\nPEP). Returns matches above the configured fuzz threshold.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "normalized_name": {
                    "type": "string"
                },
                "lists": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "ofac_sdn",
                            "un_consolidated",
                            "eu_consolidated",
                            "hmt",
                            "institution_pep"
                        ]
                    }
                },
                "threshold": {
                    "type": "number",
                    "default": 0.92,
                    "description": "Jaro-Winkler fuzz threshold."
                }
            },
            "required": [
                "normalized_name",
                "lists"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "matches": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "entity_id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "source_list": {
                                "type": "string"
                            },
                            "score": {
                                "type": "number"
                            },
                            "listed_on": {
                                "type": "string",
                                "format": "date"
                            },
                            "program": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/sanctions-check",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "finance",
                "finance.aml",
                "finance.kyc"
            ],
            "ohh:capability": [
                "verification",
                "safety_gating"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "swift-bic-validator",
        "title": "SWIFT BIC validator + BIC \u2192 bank metadata",
        "description": "Validate an 8 or 11-character SWIFT BIC (Bank Identifier Code) and\nresolve it to the bank's name + country + city. Used by payment-\nprocessing + KYC + AML pipelines for counterparty bank\nidentification.\n\nOffline validation uses the SWIFT BIC structure rules (bank code\n4 chars + country code 2 chars ISO 3166 + location code 2 chars +\noptional branch code 3 chars). Online lookup against bundled\nSWIFT BIC directory snapshot (refresh quarterly).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "bic_code": {
                    "type": "string",
                    "pattern": "^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$"
                }
            },
            "required": [
                "bic_code"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "is_valid": {
                    "type": "boolean"
                },
                "bic_8": {
                    "type": "string"
                },
                "bic_11": {
                    "type": "string"
                },
                "bank_code": {
                    "type": "string"
                },
                "country_iso2": {
                    "type": "string"
                },
                "location_code": {
                    "type": "string"
                },
                "branch_code": {
                    "type": "string"
                },
                "bank_name": {
                    "type": "string"
                },
                "bank_city": {
                    "type": "string"
                },
                "swift_active": {
                    "type": "boolean"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/swift-bic-validator",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "finance",
                "finance.kyc",
                "finance.aml"
            ],
            "ohh:capability": [
                "verification",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "txt2img-sdxl",
        "title": "Text-to-Image (SDXL)",
        "description": "Generic SDXL text-to-image tool. Backend-agnostic \u2014 implementations\ninclude local Diffusers, Replicate, Hugging Face Inference, fal.ai,\nTogether, or a custom OpenAPI endpoint.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string"
                },
                "negative_prompt": {
                    "type": "string"
                },
                "width": {
                    "type": "integer",
                    "default": 1024
                },
                "height": {
                    "type": "integer",
                    "default": 1024
                },
                "steps": {
                    "type": "integer",
                    "default": 30
                },
                "guidance_scale": {
                    "type": "number",
                    "default": 7.5
                },
                "seed": {
                    "type": "integer"
                }
            },
            "required": [
                "prompt"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "image_url": {
                    "type": "string"
                },
                "seed": {
                    "type": "integer"
                },
                "model": {
                    "type": "string"
                }
            }
        },
        "annotations": {
            "openWorldHint": true
        },
        "_meta": {
            "ohh:artifactId": "tool/txt2img-sdxl",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "creative"
            ],
            "ohh:capability": [
                "image_synthesis"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "usps-address-validator",
        "title": "USPS address validation",
        "description": "Proxy to the USPS Address Information API. Given a US address,\nreturns: standardized form, ZIP+4, deliverability, DPV (Delivery\nPoint Validation) status, RDI (Residential Delivery Indicator).\nUse to confirm an address is mailable before accepting it into a\ncustomer / shipping record.\n\nRequires USPS_USER_ID env var (free tier: 5 requests/sec).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "street_1": {
                    "type": "string"
                },
                "street_2": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                },
                "zip5": {
                    "type": "string"
                }
            },
            "required": [
                "street_1"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "standardized": {
                    "type": "object",
                    "properties": {
                        "street_1": {
                            "type": "string"
                        },
                        "street_2": {
                            "type": "string"
                        },
                        "city": {
                            "type": "string"
                        },
                        "state": {
                            "type": "string"
                        },
                        "zip5": {
                            "type": "string"
                        },
                        "zip4": {
                            "type": "string"
                        }
                    }
                },
                "deliverable": {
                    "type": "boolean"
                },
                "dpv_code": {
                    "type": "string",
                    "enum": [
                        "Y",
                        "D",
                        "S",
                        "N"
                    ]
                },
                "rdi": {
                    "type": "string",
                    "enum": [
                        "residential",
                        "commercial",
                        "unknown"
                    ]
                }
            }
        },
        "annotations": {
            "openWorldHint": true
        },
        "_meta": {
            "ohh:artifactId": "tool/usps-address-validator",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "retail",
                "finance",
                "government"
            ],
            "ohh:capability": [
                "verification"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "web-search",
        "title": "Web Search",
        "description": "Generic web search tool. Backend-agnostic \u2014 implementations include\nBrave, Serper, DuckDuckGo, or a self-hosted SearXNG.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string"
                },
                "max_results": {
                    "type": "integer",
                    "default": 10
                },
                "site": {
                    "type": "string",
                    "description": "Optional site: filter."
                },
                "language": {
                    "type": "string",
                    "description": "ISO 639-1 language code."
                }
            },
            "required": [
                "query"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "snippet": {
                                "type": "string"
                            },
                            "score": {
                                "type": "number"
                            }
                        }
                    }
                }
            }
        },
        "annotations": {
            "openWorldHint": true
        },
        "_meta": {
            "ohh:artifactId": "tool/web-search",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "lookup-icd10",
        "title": "ICD-10 lookup",
        "description": "Lookup an ICD-10 diagnosis code by code or label substring. Returns\ncode + label + category. Backend-agnostic; intended to bind to a\nlocal copy of the WHO ICD-10 release or to an institutional\nterminology server.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "ICD-10 code or label substring."
                },
                "max": {
                    "type": "integer",
                    "default": 10
                }
            }
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "matches": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string"
                            },
                            "label": {
                                "type": "string"
                            },
                            "category": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/lookup-icd10",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "healthcare",
                "healthcare.clinical"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "semgrep-sast-proxy",
        "title": "Semgrep SAST proxy (CWE-tagged code findings)",
        "description": "Proxy to Semgrep CLI for static-analysis code scanning. Used by\n`pipeline/code-security-review` to corroborate GREP findings with\na real SAST tool that has community-maintained rules and proper\nAST analysis. Returns CWE-tagged findings with file:line refs.\n\nImplementation defers to local semgrep CLI; no network egress.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target_path": {
                    "type": "string",
                    "description": "File or directory to scan."
                },
                "config": {
                    "type": "string",
                    "description": "Semgrep config: 'auto' OR 'p/security-audit' OR custom rule file path.",
                    "default": "p/security-audit"
                },
                "severity_filter": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "INFO",
                            "WARNING",
                            "ERROR"
                        ]
                    }
                }
            },
            "required": [
                "target_path"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "findings": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "rule_id": {
                                "type": "string"
                            },
                            "cwe": {
                                "type": "string"
                            },
                            "owasp": {
                                "type": "string"
                            },
                            "severity": {
                                "type": "string"
                            },
                            "file": {
                                "type": "string"
                            },
                            "start_line": {
                                "type": "integer"
                            },
                            "end_line": {
                                "type": "integer"
                            },
                            "message": {
                                "type": "string"
                            }
                        }
                    }
                },
                "finding_count": {
                    "type": "integer"
                },
                "elapsed_ms": {
                    "type": "integer"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/semgrep-sast-proxy",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "security",
                "security.appsec",
                "software"
            ],
            "ohh:capability": [
                "verification",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "opencorporates-lookup",
        "title": "OpenCorporates company lookup",
        "description": "Look up a company in the OpenCorporates global registry (220M+\nlegal entities). Returns: jurisdiction code, incorporation date,\ncompany status, registered address, officers, beneficial-ownership\nfilings where disclosed. Used by ESG / KYC / vendor-onboarding\npipelines to verify a counterparty is a real legal entity.\n\nFree tier: 50 queries/day. Requires OPENCORPORATES_API_KEY for\nhigher tiers.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string"
                },
                "jurisdiction_code": {
                    "type": "string",
                    "description": "ISO 3166 + sub-division, e.g. 'us_de' for Delaware, 'gb' for UK."
                },
                "company_number": {
                    "type": "string",
                    "description": "Exact lookup if known."
                },
                "include_officers": {
                    "type": "boolean",
                    "default": true
                },
                "include_filings": {
                    "type": "boolean",
                    "default": false
                }
            },
            "oneOf": [
                {
                    "required": [
                        "company_name"
                    ]
                },
                {
                    "required": [
                        "company_number",
                        "jurisdiction_code"
                    ]
                }
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "company_number": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "jurisdiction_code": {
                                "type": "string"
                            },
                            "incorporation_date": {
                                "type": "string",
                                "format": "date"
                            },
                            "status": {
                                "type": "string"
                            },
                            "company_type": {
                                "type": "string"
                            },
                            "registered_address": {
                                "type": "string"
                            },
                            "officers": {
                                "type": "array"
                            }
                        }
                    }
                },
                "total_count": {
                    "type": "integer"
                }
            }
        },
        "annotations": {
            "openWorldHint": true
        },
        "_meta": {
            "ohh:artifactId": "tool/opencorporates-lookup",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "finance",
                "finance.kyc",
                "compliance",
                "esg",
                "supply_chain"
            ],
            "ohh:capability": [
                "verification",
                "retrieval"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "mitre-attack-mapper",
        "title": "MITRE ATT&CK technique mapper",
        "description": "Map free-text TTPs to MITRE ATT&CK technique IDs (T1234.xxx).\nReturns the matched technique + tactic + sub-techniques + KEV\nstatus if any associated CVE is on the CISA Known Exploited\nVulnerabilities catalog.\n\nUses the latest ATT&CK Enterprise matrix snapshot bundled at\nknowledge-pack/mitre-attack-sample. For live ATT&CK STIX feed,\nconfigure `mitre_navigator_endpoint` env var.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ttp_text": {
                    "type": "string",
                    "description": "Free-text TTP description, e.g. 'lateral movement via WMI'."
                },
                "return_subtechs": {
                    "type": "boolean",
                    "default": true
                },
                "check_kev": {
                    "type": "boolean",
                    "default": true,
                    "description": "Cross-check any T-id's associated CVEs against CISA KEV."
                },
                "threshold": {
                    "type": "number",
                    "default": 0.7
                }
            },
            "required": [
                "ttp_text"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "matches": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "technique_id": {
                                "type": "string"
                            },
                            "technique_name": {
                                "type": "string"
                            },
                            "tactic": {
                                "type": "string"
                            },
                            "score": {
                                "type": "number"
                            },
                            "kev_status": {
                                "type": "string",
                                "enum": [
                                    "none",
                                    "in_kev",
                                    "associated_cve_in_kev"
                                ]
                            }
                        }
                    }
                },
                "best_match": {
                    "type": "object"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/mitre-attack-mapper",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "security",
                "threat_intelligence",
                "threat_intelligence.ttp"
            ],
            "ohh:capability": [
                "verification",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "presidio-pii-detect",
        "title": "Microsoft Presidio PII detection proxy",
        "description": "Proxy to Microsoft Presidio Analyzer for PII detection.\nSubstantially more thorough than `processor/redact-pii-text`\nregex baseline \u2014 supports 30+ entity types across multiple\nlanguages, ML-backed NER for PERSON names + LOCATION, custom\nrecognizers, denylist anchors, AnalyzerEngine + RecognizerRegistry.\n\nPair with `processor/redact-pii-text` for fast first-pass +\nPresidio for thorough second-pass on high-stakes outputs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string"
                },
                "entities": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Subset of PERSON / EMAIL_ADDRESS / PHONE_NUMBER / IBAN_CODE / US_SSN / CREDIT_CARD / DATE_TIME / LOCATION / MEDICAL_LICENSE / US_DRIVER_LICENSE / IP_ADDRESS / NRP / UK_NHS / etc."
                },
                "language": {
                    "type": "string",
                    "default": "en"
                },
                "score_threshold": {
                    "type": "number",
                    "default": 0.5
                },
                "return_decision_process": {
                    "type": "boolean",
                    "default": false
                }
            },
            "required": [
                "text"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "detected_entities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "entity_type": {
                                "type": "string"
                            },
                            "start": {
                                "type": "integer"
                            },
                            "end": {
                                "type": "integer"
                            },
                            "score": {
                                "type": "number"
                            },
                            "recognizer": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            }
                        }
                    }
                },
                "entity_count_by_type": {
                    "type": "object"
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/presidio-pii-detect",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "healthcare",
                "finance",
                "insurance",
                "government"
            ],
            "ohh:capability": [
                "anonymization",
                "verification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "transaction-graph-query",
        "title": "Transaction graph query",
        "description": "Query a transaction-graph store for one-hop or multi-hop paths\nbetween accounts / entities. Used by AML harnesses to find shell\nlayering, circular flows, and rapid-in-rapid-out patterns.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "seed_account": {
                    "type": "string"
                },
                "direction": {
                    "type": "string",
                    "enum": [
                        "in",
                        "out",
                        "both"
                    ],
                    "default": "both"
                },
                "max_hops": {
                    "type": "integer",
                    "default": 2
                },
                "time_window_days": {
                    "type": "integer",
                    "default": 14
                },
                "min_amount_usd": {
                    "type": "number",
                    "default": 0
                }
            },
            "required": [
                "seed_account"
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "kind": {
                                "type": "string",
                                "enum": [
                                    "account",
                                    "entity",
                                    "vessel"
                                ]
                            },
                            "country": {
                                "type": "string"
                            },
                            "risk_score": {
                                "type": "number"
                            }
                        }
                    }
                },
                "edges": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "src": {
                                "type": "string"
                            },
                            "dst": {
                                "type": "string"
                            },
                            "amount_usd": {
                                "type": "number"
                            },
                            "ts": {
                                "type": "string",
                                "format": "date-time"
                            },
                            "kind": {
                                "type": "string",
                                "enum": [
                                    "wire",
                                    "ach",
                                    "card",
                                    "cash",
                                    "internal"
                                ]
                            }
                        }
                    }
                }
            }
        },
        "annotations": {
            "readOnlyHint": true,
            "destructiveHint": false
        },
        "_meta": {
            "ohh:artifactId": "tool/transaction-graph-query",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "finance",
                "finance.aml"
            ],
            "ohh:capability": [
                "retrieval",
                "reasoning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "google-geocode",
        "title": "Google Maps Geocoding (address \u2192 lat/lng)",
        "description": "Forward and reverse geocoding via Google Maps Geocoding API.\nReturns lat/lng + place_id + formatted_address + address_components\n(street_number / route / locality / admin_area_level_1 / country).\n\nRequires GOOGLE_MAPS_API_KEY env var. Free tier: ~$0 up to $200/mo.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "description": "Forward geocoding: free-form address."
                },
                "latlng": {
                    "type": "string",
                    "description": "Reverse geocoding: 'lat,lng' string."
                },
                "region": {
                    "type": "string",
                    "description": "ccTLD-style region biasing, e.g. 'us'."
                },
                "language": {
                    "type": "string",
                    "default": "en"
                }
            },
            "oneOf": [
                {
                    "required": [
                        "address"
                    ]
                },
                {
                    "required": [
                        "latlng"
                    ]
                }
            ]
        },
        "outputSchema": {
            "type": "object",
            "properties": {
                "results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "place_id": {
                                "type": "string"
                            },
                            "formatted_address": {
                                "type": "string"
                            },
                            "location": {
                                "type": "object",
                                "properties": {
                                    "lat": {
                                        "type:\"number\"": null
                                    },
                                    "lng": {
                                        "type:\"number\"": null
                                    }
                                }
                            },
                            "location_type": {
                                "type": "string",
                                "enum": [
                                    "ROOFTOP",
                                    "RANGE_INTERPOLATED",
                                    "GEOMETRIC_CENTER",
                                    "APPROXIMATE"
                                ]
                            },
                            "address_components": {
                                "type": "array"
                            }
                        }
                    }
                },
                "status": {
                    "type": "string",
                    "enum": [
                        "OK",
                        "ZERO_RESULTS",
                        "OVER_QUERY_LIMIT",
                        "REQUEST_DENIED",
                        "INVALID_REQUEST",
                        "UNKNOWN_ERROR"
                    ]
                }
            }
        },
        "annotations": {
            "openWorldHint": true
        },
        "_meta": {
            "ohh:artifactId": "tool/google-geocode",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "retail",
                "real_estate",
                "transportation"
            ],
            "ohh:capability": [
                "verification",
                "extraction"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "checklist-evaluator",
        "title": "Checklist evaluator (GO/NO-GO)",
        "description": "Reads a named procedural checklist (knowledge-pack/technician-checklists record) plus a candidate input, returns per-item disposition (verified|unverified|nogo) + overall verdict (go|nogo). NO-GO triggers override otherwise-clean inputs.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/checklist-evaluator",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "compliance",
                "healthcare",
                "aviation",
                "energy",
                "construction"
            ],
            "ohh:capability": [
                "safety_gating",
                "evaluation",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "hyde-query-expander",
        "title": "HyDE query expander",
        "description": "Hypothetical Document Embeddings (HyDE): generate a hypothetical\n*answer* to the user's query, then embed that hypothetical answer\nfor retrieval instead of (or in addition to) the original query.\nOften improves recall on questions that don't share vocabulary\nwith the source documents.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/hyde-query-expander",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "retrieval",
                "generation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "two-time-retrieval",
        "title": "Two-time retrieval (refine query, re-retrieve)",
        "description": "Retrieve top-K with the raw query, ask an LLM to compose a refined\nquery incorporating what was found, then re-retrieve. Final retrieval\nset is the second pass (or union of both, deduplicated). Classic\nKaggle \"EEDI two-time retrieval\" shape \u2014 boosts recall on math-\nmisconception problems where the right answer needs concept-level\nreformulation.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/two-time-retrieval",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "education"
            ],
            "ohh:capability": [
                "retrieval",
                "reasoning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "sub-question-decomposer",
        "title": "Sub-question decomposer",
        "description": "Break a compound question into N atomic sub-questions, each\nindependently answerable. Used by `pipeline/multi-doc-qa-subquestion`\nand similar LlamaIndex SubQuestionQueryEngine flows.\n\nReturns the sub-question list + a small dependency graph (e.g. Q3\ndepends on Q1's answer). The pipeline runtime can then schedule\nretrieval / answering with the right ordering.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/sub-question-decomposer",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "reasoning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "nsfw-image-classifier",
        "title": "NSFW image classifier",
        "description": "Lightweight NSFW image classifier (CLIP-based zero-shot or a\nfine-tuned head). Returns probability of NSFW content; pipelines\nbind to a threshold via the calling rule pack.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/nsfw-image-classifier",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "creative",
                "media"
            ],
            "ohh:capability": [
                "safety_gating"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "prompt-injection-detector",
        "title": "Prompt-injection detector",
        "description": "Detect prompt-injection / jailbreak attempts in user input,\nretrieved documents, or tool results. Two-tier: a fast regex /\nclassifier first pass plus an optional small-model classifier\nsecond pass.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/prompt-injection-detector",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "security"
            ],
            "ohh:capability": [
                "safety_gating",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "context-window-packer",
        "title": "Context-window packer (Lost-in-the-middle aware)",
        "description": "Reorganize retrieved chunks into the model's context window so the\nmost important content lands at the BEGINNING and END of the window\n(Liu et al. 2023 \"Lost in the Middle\"). Also enforces:\n  - token budget cap\n  - per-source dedup\n  - chunk-priority ordering (rerank score \u2192 recency \u2192 source authority)\n  - explicit chunk delimiters with index labels for citation\nReturns the packed context string + chunk-index \u2192 source map.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/context-window-packer",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "inject-datetime-locale",
        "title": "Inject datetime + locale into prompt",
        "description": "Replace placeholders like `{{now}}`, `{{today}}`, `{{user_timezone}}`,\n`{{user_locale}}`, `{{user_currency}}` in the prompt template with the\nactual values at request time. Fixes the \"stale knowledge cutoff\" issue\nwhere the model otherwise has no idea what today's date is.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/inject-datetime-locale",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "inject-output-schema",
        "title": "Inject output schema directive",
        "description": "Render a target JSON Schema (or Pydantic model) into the prompt as\nan instruction the model is asked to follow. Pairs with\n`processor/json-schema-repair` on the response side: if the model's\noutput doesn't conform, the loop processor can re-prompt with the\nvalidation error appended.\n\nThree injection styles:\n  - `schema_only`: bare JSON Schema in a fenced code block.\n  - `schema_plus_example`: schema + a minimal conforming example.\n  - `constrained_grammar_marker`: hints for outlines / xgrammar /\n    llama.cpp grammar-constrained decoding.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/inject-output-schema",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "ai"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "self-refine-critique",
        "title": "Self-Refine critique loop",
        "description": "Critique-and-revise loop (Madaan et al. 2023). The same model first\ndrafts an answer, then critiques its own draft against a rubric,\nthen revises. Iterates up to `max_iterations`. Useful when a single\npass produces verbose or weakly-grounded output.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/self-refine-critique",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "reasoning",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "llm-judge",
        "title": "LLM-as-judge",
        "description": "Generic LLM-as-judge wrapper. Given (candidate response, rubric,\ncontext), returns a per-dimension score with rationale and a\nweighted-sum overall score. Independent of the model under review \u2014\nthe judge sits outside that model's reasoning trace.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/llm-judge",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "evaluation"
            ],
            "ohh:trustBoundary": "mixed"
        }
    },
    {
        "name": "community-summary-mapreduce",
        "title": "Community-summary map-reduce (GraphRAG global)",
        "description": "Per-community map step (LLM summarizes each Leiden community), then\nreduce step combines partial answers across communities. The core\nprimitive of GraphRAG's global-search mode.\n\nVerified by Open Harness Hub clone:\n`microsoft/graphrag/packages/graphrag/graphrag/query/structured_search/global_search/`.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/community-summary-mapreduce",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "cross_industry"
            ],
            "ohh:capability": [
                "summarization",
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "multi-vector-fusion",
        "title": "Multi-vector / multi-query fusion (RRF + weighted)",
        "description": "Fuse N ranked candidate lists from independent retrievers (sparse +\ndense + graph + cross-encoder reranker output) via Reciprocal Rank\nFusion or weighted score blending. Returns a single deduped ranked\nlist.\n\nVerified by Open Harness Hub clones: shape appears in\n`Raudaschl/rag-fusion`, `superlinear-ai/raglite/_search.py`, and\n`microsoft/graphrag/global_search/`.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/multi-vector-fusion",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "cross_industry"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "skeleton-outliner",
        "title": "Skeleton outliner (Skeleton-of-Thought)",
        "description": "Generate a skeleton (bullet outline) for a long-form output, then\nreturn the outline so parallel sub-expansion can fan out per bullet.\nUsed by Skeleton-of-Thought, STORM, and any pattern that benefits\nfrom outline-then-expand.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/skeleton-outliner",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "media",
                "education"
            ],
            "ohh:capability": [
                "generation",
                "planning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "intent-dispatcher",
        "title": "Intent dispatcher",
        "description": "Classify an incoming message into one of N intents and route to the\nappropriate downstream pipeline. Backend can be a classifier rule\npack, a small local model, or a keyword router.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/intent-dispatcher",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "routing",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "cost-ceiling-gate",
        "title": "Cost ceiling gate",
        "description": "Reject a pipeline run if the predicted USD cost exceeds the budget\nconfigured for the calling pipeline / user. Uses token-count\nestimates + adapter pricing to predict cost.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/cost-ceiling-gate",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "safety_gating"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "concept-graph-extractor",
        "title": "Concept graph extractor",
        "description": "Extract typed concept-graph nodes + edges from chunked text. Node types: concept, term, person, dataset, method, equation. Edge types: depends_on, cited_by, sub_concept, contradicts, defined_in. Each node + edge carries a (page, span) source anchor.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/concept-graph-extractor",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "education",
                "research",
                "esg",
                "compliance",
                "healthcare"
            ],
            "ohh:capability": [
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "redact-pii-text",
        "title": "Redact PII from text (English-centric, MS Presidio-compatible)",
        "description": "Strip PII from free-form text before downstream LLM calls or\nhub sharing. Detects: email, phone, IBAN, SSN, passport,\nnational-ID, full names (NER), street addresses, dates of birth,\nmedical record numbers, and the 18 HIPAA Safe Harbor identifiers.\n\nDrop-in replacement for raw text in any pipeline whose\n`lifecycle_position` \u2265 pre_api. Replaces detected entities with\n`[REDACTED:<TYPE>]` placeholders; preserves text shape so downstream\nparsing still works.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/redact-pii-text",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "healthcare",
                "finance",
                "esg"
            ],
            "ohh:capability": [
                "anonymization",
                "safety_gating"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "runtime-tool-selector",
        "title": "Runtime tool selector (Toolformer / pydantic-ai)",
        "description": "Given a user query + a large registry of tools, semantically select\nthe top-K most likely-relevant tools to expose to the model. Avoids\noverflowing the context window with every tool definition when only\na few apply.\n\nVerified by Open Harness Hub clone: implemented at\n`pydantic/pydantic-ai/_tool_search.py` (Toolformer-style).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/runtime-tool-selector",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "cross_industry"
            ],
            "ohh:capability": [
                "routing",
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "reasoning-framework-selector",
        "title": "Reasoning framework selector",
        "description": "Pick a reasoning framework (CoT / ReAct / Tree-of-Thoughts /\nSkeleton-of-Thought / Program-of-Thought / Self-Consistency / none)\nbased on the task profile. Cheap heuristic up front; can also call a\nsmall classifier model.\n\nSelector heuristics:\n  - CoT for multi-step math / logic, deterministic answer expected\n  - Self-Consistency on top of CoT for arithmetic / olympiad-level\n  - ReAct for tool-use loops\n  - Tree-of-Thoughts for exploratory planning with branching\n  - SoT for parallelizable structured outputs (lists, tables, code skeletons)\n  - PoT for problems best expressed as Python\n  - none for simple lookup / classification",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/reasoning-framework-selector",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "ai"
            ],
            "ohh:capability": [
                "routing",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "persona-set-generator",
        "title": "Persona-set generator (STORM)",
        "description": "Spawn N personas with distinct perspectives on a topic. Used by\nSTORM's multi-perspective curation and by multi-agent debate\npipelines. Each persona carries a role, an angle, prior knowledge\ncues, and a few biased priors the simulated dialogue can surface.\n\nVerified by Open Harness Hub clone:\n`stanford-oval/storm/knowledge_storm/storm_wiki/modules/persona_generator.py`.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/persona-set-generator",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "media",
                "education"
            ],
            "ohh:capability": [
                "generation",
                "planning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "iso-country-normalize",
        "title": "ISO country code normalize (alpha-2 / alpha-3 / numeric / name)",
        "description": "Resolve any country reference \u2014 alpha-2, alpha-3, numeric, English\nname, French name, common alias \u2014 to canonical ISO 3166-1 codes.\nReturns alpha-2, alpha-3, numeric, English short name, and the\nISO 3166-2 sub-division code if a region was specified.\n\nBacked by the ISO 3166 data bundled at knowledge-pack/iso-country-codes.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/iso-country-normalize",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "verification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "pdf-extract-with-ocr-fallback",
        "title": "PDF extract with OCR fallback (CiteMind shape)",
        "description": "Extract embedded PDF text page by page; fall back to OCR (Tesseract / PaddleOCR / similar) for pages whose embedded-text yield is below threshold (scanned pages, image-heavy figures).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/pdf-extract-with-ocr-fallback",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "education",
                "compliance",
                "legal",
                "research"
            ],
            "ohh:capability": [
                "format_conversion",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "date-parse-multiformat",
        "title": "Date parse multi-format \u2192 ISO 8601",
        "description": "Parse any date string in 50+ common formats (MM/DD/YYYY, DD/MM/YYYY,\nYYYY-MM-DD, Mar 5 2025, 5-Mar-25, 1709589600 epoch, ISO 8601\nfragments, RFC 2822) into a normalized ISO 8601 datetime. Resolves\nambiguous M/D order using locale hint. Preserves timezone if\ngiven, defaults to UTC otherwise.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/date-parse-multiformat",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "address-parse-standardize",
        "title": "Address parse + standardize (USPS Pub 28 / libpostal)",
        "description": "Parse a free-form postal address into components (street_number,\nstreet_name, suite, city, state, postal_code, country) and\nstandardize them to USPS Pub 28 + libpostal conventions. Handles\ninternational addresses via libpostal's CRF parser.\n\nOutput components are normalized: state \u2192 2-letter abbrev,\nstreet_type expanded then re-abbreviated, suite/apt normalized.\nUsed as a pre-step for geocoding + dedup + USPS deliverable check.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/address-parse-standardize",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "page-aware-chunker",
        "title": "Page-aware chunker",
        "description": "Split page-extracted text into ~800-token chunks with 120-token overlap; preserve the (page, span) coordinates on every chunk so downstream answers can cite back to the page + span.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/page-aware-chunker",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "education",
                "research",
                "compliance"
            ],
            "ohh:capability": [
                "format_conversion",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "pdf-to-text",
        "title": "PDF to text",
        "description": "Convert a PDF (extractable layer + optional OCR fallback) into plain\ntext with page breaks preserved. Returns text plus per-page byte\noffsets so downstream chunkers can attribute chunks back to pages.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/pdf-to-text",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "phone-normalize-e164",
        "title": "Phone number normalize \u2192 E.164 (Google libphonenumber)",
        "description": "Parse free-form phone numbers into E.164 international format\n(+CCNNNNNNNNNNNN) using Google libphonenumber conventions.\nReturns the E.164 string + country code + number type (mobile /\nfixed-line / VoIP / toll-free) + validity boolean. Handles\ncommon formatting variants (spaces, dashes, parens, country\ncodes spelled out, extensions).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/phone-normalize-e164",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "verification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "structured-to-prose",
        "title": "Structured JSON \u2192 prose normalizer (for GREP-style rule packs)",
        "description": "Walk a JSON object and emit one prose-like line per leaf value,\nflattening dict keys into space-separated labels. The output shape\nis what GREP-family rule packs (regex on natural-language prose)\nexpect \u2014 converting structured supplier disclosures, audit\nreports, or KYC packets into a form where pattern detection\nworks correctly.\n\nWithout this step, patterns like `\\b(passport)\\s+(held|retained)`\nmiss \"passport_location: Held by the workshop\" because the\nunderscore-separated key prevents direct adjacency. The processor\nemits `passport location: Held by the workshop` \u2014 and the pattern\nfires correctly.\n\nUsed by `pipeline/supplier-policy-grading` between the PII-\nredaction step and the GREP step.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/structured-to-prose",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "esg",
                "supply_chain",
                "compliance",
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "name-canonicalize",
        "title": "Person-name canonicalize (Western + East-Asian)",
        "description": "Canonicalize a person name string into structured components:\ngiven_name, family_name, middle_names, suffix, honorific. Handles\nthe East-Asian convention where family name comes first; Spanish\n/ Portuguese double-family-name; Arabic / Hebrew patronymics;\nhonorifics (Dr / Sir / Hon). Output Title-Cases each component.\n\nNEVER assigns gender from name (this is a known bias trap).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/name-canonicalize",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "audio-to-text-whisper",
        "title": "Audio to text (Whisper)",
        "description": "Speech-to-text via a Whisper-family model. Returns transcript +\nper-segment timestamps + detected language. Wraps `openai-whisper`,\n`faster-whisper`, or `distil-whisper` based on the implementation\nchosen at runtime.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/audio-to-text-whisper",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "translation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "embedder-minilm",
        "title": "Text embedder (MiniLM-L6-v2)",
        "description": "Generate 384-dimensional text embeddings using\n`sentence-transformers/all-MiniLM-L6-v2`. Suitable for catalog\nsemantic search, RAG retrieval, and de-duplication. Replace with a\nhigher-dim embedder for production semantic retrieval.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/embedder-minilm",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "embedding"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "local-embedder",
        "title": "Local embedder (Ollama / nomic / mxbai)",
        "description": "Embed text chunks via a local embedding model (Ollama nomic-embed-text / mxbai-embed-large / etc.). No network round-trip; embeddings stored locally.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/local-embedder",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "education",
                "research",
                "compliance",
                "privacy"
            ],
            "ohh:capability": [
                "extraction",
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "iterative-revise-loop",
        "title": "Iterative revise loop",
        "description": "The \"send the response back to the LLM with accumulating context\" primitive.\nLoops:\n  1. Run an inner harness call.\n  2. Run one or more verification processors on the response.\n  3. If any verifier fails (citation coverage, schema, factuality,\n     safety), append the failure as additional context and call the\n     inner harness again.\n  4. Stop when (a) all verifiers pass, (b) max_iterations hit, or\n     (c) cost ceiling breached.\n\nThis is the key primitive for self-correction loops: Self-Refine,\nConstitutional-AI critique-revise, Self-RAG retrieve-then-judge,\nCorrective-RAG with knowledge refinement, Reflexion. Distinct from\n`processor/self-refine-critique` (which is a single critique-revise\npair); this primitive is the GENERIC LOOP that any verifier list can\ndrive.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/iterative-revise-loop",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "reasoning",
                "verification",
                "agent_loop"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "llmlingua-context-compressor",
        "title": "LLMLingua context compressor",
        "description": "Compress long context (retrieved RAG chunks or prior conversation turns)\nby selectively pruning low-information tokens before the model sees\nthem. Implementations include LLMLingua, LongLLMLingua, and\nSelective-Context.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/llmlingua-context-compressor",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "action-sampler-multi-rollout",
        "title": "Action sampler \u2014 N parallel rollouts",
        "description": "Sample N independent action trajectories for an agent task; return\nthe trajectories + final-state candidates for downstream judging.\nThe N candidates can be reviewed by a separate judge processor to\npick the best.\n\nVerified by Open Harness Hub clone:\n`SWE-agent/sweagent/agent/action_sampler.py`.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/action-sampler-multi-rollout",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "software"
            ],
            "ohh:capability": [
                "agent_loop",
                "planning"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "self-consistency-sampler",
        "title": "Self-consistency sampler",
        "description": "Run N parallel samples of a chain-of-thought reasoning prompt, then\nmajority-vote on the final answer (Wang et al. 2023). Robust to\narithmetic and reasoning errors that a single sample would miss.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/self-consistency-sampler",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "reasoning",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "hybrid-bm25-vector-retrieve",
        "title": "Hybrid BM25 + vector retrieve",
        "description": "Combine BM25 lexical scoring with vector cosine similarity (reciprocal rank fusion) for retrieval. Returns top-k chunks with merged ranking, preserving page anchors for citation.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/hybrid-bm25-vector-retrieve",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "education",
                "research",
                "compliance"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "cross-encoder-reranker",
        "title": "Cross-encoder reranker",
        "description": "Re-rank a list of retrieved candidates with a cross-encoder model\n(BAAI/bge-reranker-base, Cohere rerank-v3, or similar). Takes top-N\ncandidates from a hybrid retriever and returns the top-K most\nrelevant to the query. Typically used between hybrid retrieval and\ncontext-window assembly.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/cross-encoder-reranker",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "ai"
            ],
            "ohh:capability": [
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "entity-resolution-link",
        "title": "Entity resolution: cluster records into entities",
        "description": "Given N records, cluster those that refer to the same real-world\nentity (person, organization, address). Combines:\n 1. Blocking on canonical fields (zip, last name initial, alpha-2\n    country)\n 2. Pairwise similarity using Jaro-Winkler (names), Levenshtein\n    (addresses), exact match (emails / SSN / IDs)\n 3. Active record linkage with a learned threshold\n 4. Transitive closure into entity clusters\n\nOutputs cluster IDs + per-cluster confidence + record-pairs above\nthe merge threshold.\n\nImplements the Fellegi-Sunter (1969) probabilistic record-linkage\nmodel with modern blocking + locality-sensitive hashing.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/entity-resolution-link",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "finance",
                "healthcare",
                "government",
                "compliance"
            ],
            "ohh:capability": [
                "verification",
                "extraction",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "verify-tool-validate-criterion",
        "title": "Tool-validation success-criterion evaluator",
        "description": "Evaluates one `kind: tool_validate` success criterion. Invokes\nan external tool (e.g. `tool/json-schema-validator`,\n`tool/run-unit-tests`, `tool/iban-checker`) against the target.\nPasses iff the tool returns success.\n\nUse for: 'output validates against schemas/X.schema.json',\n'generated code passes pytest', 'extracted IBAN passes mod-97',\n'rendered HTML passes axe-core accessibility audit'.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/verify-tool-validate-criterion",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "evaluation",
                "tool_use"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "hallucination-scorer",
        "title": "Hallucination scorer (SelfCheckGPT-style)",
        "description": "Score per-sentence hallucination probability by sampling N alternative\ngenerations from the same model, then measuring semantic agreement\nbetween them. Sentences that vary widely across samples are flagged as\nlikely hallucinations. Based on SelfCheckGPT (Manakul et al. 2023).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/hallucination-scorer",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "verify-composite-criterion",
        "title": "Composite (AND/OR/NOT) success-criterion evaluator",
        "description": "Evaluates one `kind: composite` success criterion. Combines child\ncriteria with AND / OR / NOT semantics. Children may themselves be\ncomposite \u2014 arbitrarily deep nesting allowed. Short-circuits where\npossible (AND stops at first failure; OR stops at first pass).\n\nUse to express: '(critical-red-flags-found AND remediation-proposed)\nOR clean-baseline', 'PHI-redacted AND (rubric-score >= 0.7 OR\nhuman-reviewed)', etc.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/verify-composite-criterion",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "verify-regex-criterion",
        "title": "Regex success-criterion evaluator",
        "description": "Evaluates one `kind: regex` success criterion. Given a target\npath (resolved from the pipeline trace) + a pattern + a\n`must_match` flag, returns a pass/fail record with the matched\nspan (if any).\n\nUse in `success_criteria:` lists alongside other criterion kinds\n(semantic / llm_judge / deterministic / tool_validate / composite).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/verify-regex-criterion",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "citation-coverage",
        "title": "Citation coverage verifier",
        "description": "Verify that every factual sentence in a response carries at least\none citation marker (e.g. `[1]`, `[smith-2026]`). Returns coverage\nratio and a list of uncited sentences for re-prompt.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/citation-coverage",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "official-sources-checker",
        "title": "Official-sources analyzer",
        "description": "Verify retrieved candidates against an allowlist of authoritative\nsources (gov, intergovernmental, academic, standards bodies).\nReturns per-candidate flags:\n  - is_official: bool\n  - authority_tier: enum [primary, secondary, tertiary, blog, unknown]\n  - jurisdiction_match: did the source's jurisdiction match the\n    query's geographic scope?\n  - freshness_ok: source date within the requested window?\n  - cross_referenced: does another official source corroborate?\nPairs naturally with `rule-pack/web-search-allowlist-default` and\nthe DueCare `official_sources` layer pattern.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/official-sources-checker",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry",
                "media",
                "government",
                "healthcare",
                "finance"
            ],
            "ohh:capability": [
                "verification"
            ],
            "ohh:trustBoundary": "external"
        }
    },
    {
        "name": "verify-deterministic-criterion",
        "title": "Deterministic comparison success-criterion evaluator",
        "description": "Evaluates one `kind: deterministic` success criterion. Resolves a\ntarget value from the pipeline trace and applies a comparison\noperator (>, >=, <, <=, ==, !=, in, not_in, is_truthy, is_falsy)\nagainst an expected value.\n\nUse for: 'pipeline output count > 5', 'severity_counts.critical == 0',\n'rule-pack fire count < 3', etc.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/verify-deterministic-criterion",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "document-grader",
        "title": "Per-document relevance grader (Self-RAG)",
        "description": "Score each retrieved document for relevance to the user query. Emits\nper-doc grade \u2208 {relevant, irrelevant, ambiguous} with a confidence\nscore. Used by Self-RAG and CRAG to filter or trigger fallback.\n\nVerified by Open Harness Hub clone: pattern shows up in Self-RAG's\nreflection-token approach and is the canonical first step of\nCorrective-RAG.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/document-grader",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "ai",
                "cross_industry"
            ],
            "ohh:capability": [
                "verification",
                "classification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "cost-meter",
        "title": "Cost meter",
        "description": "Emit per-call USD cost accounting given (adapter_ref, input_tokens,\noutput_tokens, cached_tokens). Resolves the adapter's pricing card,\nmultiplies, and writes a metering row to the configured sink.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/cost-meter",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "evaluation"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "json-schema-repair",
        "title": "JSON Schema repair + validate",
        "description": "Parse and repair JSON inside a model response, then validate against\na JSON Schema. On failure, returns `valid: false` plus the schema\nerrors so the upstream harness can re-prompt with the diff.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/json-schema-repair",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion",
                "verification"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "memory-conversational-store",
        "title": "Conversational memory store",
        "description": "Read / write conversational memory keyed by (user_id, session_id).\nStores the last N turns plus a compressed summary for older turns.\nPluggable backend: SQLite (default), Redis, Postgres, or DynamoDB.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/memory-conversational-store",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "memory"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "recipient-tone-history",
        "title": "Recipient tone-history loader",
        "description": "Load the user's prior N email / chat exchanges with a specific\nrecipient, summarize the tone signals (formality, length,\nwarmth, sign-off style), and emit a tone-profile that downstream\ndraft-generation steps consult. Avoids drafting in the wrong\nregister (formal to a longtime peer, casual to a board member).",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": false
        },
        "_meta": {
            "ohh:artifactId": "processor/recipient-tone-history",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "personal_productivity"
            ],
            "ohh:capability": [
                "memory",
                "extraction"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "preference-loader",
        "title": "User preference loader",
        "description": "Load the user's preference file from\n`knowledge-pack/user-preference-schema` (or per-user overrides),\nresolve any inheritance from defaults, and emit a structured\npreference object that downstream steps can consult.\n\nUsed at the start of any personal-assistant harness execution\nto ensure preferences are HONORED, not assumed.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/preference-loader",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "personal_productivity",
                "cross_industry"
            ],
            "ohh:capability": [
                "memory",
                "retrieval"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "calendar-slot-finder",
        "title": "Calendar slot finder (preference-aware)",
        "description": "Given the user's calendar + their preferences (no-meeting hours,\nfocus blocks, preferred meeting hours), find N candidate slots\nfor a new meeting. Honors duration, time-zone, attendee\navailability, and the user's hard rules.\n\nRefuses to suggest slots in no-meeting windows unless the\ncaller has explicitly authorized override.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/calendar-slot-finder",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "personal_productivity"
            ],
            "ohh:capability": [
                "reasoning",
                "memory"
            ],
            "ohh:trustBoundary": "local"
        }
    },
    {
        "name": "recursive-character-chunker",
        "title": "Recursive character chunker",
        "description": "Split text into chunks using a recursive character splitter\n(LangChain-style) that prefers paragraph \u2192 sentence \u2192 word\nboundaries. Returns chunks with overlap + per-chunk byte offsets so\ncitations can point back to the source.",
        "inputSchema": {
            "type": "object",
            "additionalProperties": false
        },
        "annotations": {
            "readOnlyHint": true
        },
        "_meta": {
            "ohh:artifactId": "processor/recursive-character-chunker",
            "ohh:version": "0.1.0",
            "ohh:license": "MIT",
            "ohh:industry": [
                "cross_industry"
            ],
            "ohh:capability": [
                "format_conversion"
            ],
            "ohh:trustBoundary": "local"
        }
    }
]

# ── Server wiring ──────────────────────────────────────────────────────────

server = Server("open-harness-hub")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name=t["name"],
            title=t.get("title"),
            description=t.get("description", ""),
            inputSchema=t["inputSchema"],
        )
        for t in TOOLS
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    handler = HANDLERS.get(name)
    if handler is None:
        return [TextContent(type="text", text=f"unknown tool: {name!r}")]
    result = await handler(arguments)
    if not isinstance(result, str):
        result = json.dumps(result, indent=2)
    return [TextContent(type="text", text=result)]


# ── Tool implementations (TODO: fill these in) ─────────────────────────────

async def _run_json_schema_validator(args: dict[str, Any]) -> Any:
    """JSON Schema 2020-12 validator — Validates a candidate JSON object against a JSON Schema 2020-12"""
    # TODO: implement 'tool/json-schema-validator'
    return {'received': args, 'tool': 'json-schema-validator', 'status': 'stub'}


async def _run_cbp_wro_lookup(args: dict[str, Any]) -> Any:
    """US CBP Withhold Release Order + UFLPA Entity List lookup — Check a supplier name + geography against:"""
    # TODO: implement 'tool/cbp-wro-lookup'
    return {'received': args, 'tool': 'cbp-wro-lookup', 'status': 'stub'}


async def _run_sanctions_check(args: dict[str, Any]) -> Any:
    """Sanctions list check — Check a normalized entity name against one or more sanctions lists"""
    # TODO: implement 'tool/sanctions-check'
    return {'received': args, 'tool': 'sanctions-check', 'status': 'stub'}


async def _run_swift_bic_validator(args: dict[str, Any]) -> Any:
    """SWIFT BIC validator + BIC → bank metadata — Validate an 8 or 11-character SWIFT BIC (Bank Identifier Code) and"""
    # TODO: implement 'tool/swift-bic-validator'
    return {'received': args, 'tool': 'swift-bic-validator', 'status': 'stub'}


async def _run_txt2img_sdxl(args: dict[str, Any]) -> Any:
    """Text-to-Image (SDXL) — Generic SDXL text-to-image tool. Backend-agnostic — implementations"""
    # TODO: implement 'tool/txt2img-sdxl'
    return {'received': args, 'tool': 'txt2img-sdxl', 'status': 'stub'}


async def _run_usps_address_validator(args: dict[str, Any]) -> Any:
    """USPS address validation — Proxy to the USPS Address Information API. Given a US address,"""
    # TODO: implement 'tool/usps-address-validator'
    return {'received': args, 'tool': 'usps-address-validator', 'status': 'stub'}


async def _run_web_search(args: dict[str, Any]) -> Any:
    """Web Search — Generic web search tool. Backend-agnostic — implementations include"""
    # TODO: implement 'tool/web-search'
    return {'received': args, 'tool': 'web-search', 'status': 'stub'}


async def _run_lookup_icd10(args: dict[str, Any]) -> Any:
    """ICD-10 lookup — Lookup an ICD-10 diagnosis code by code or label substring. Returns"""
    # TODO: implement 'tool/lookup-icd10'
    return {'received': args, 'tool': 'lookup-icd10', 'status': 'stub'}


async def _run_semgrep_sast_proxy(args: dict[str, Any]) -> Any:
    """Semgrep SAST proxy (CWE-tagged code findings) — Proxy to Semgrep CLI for static-analysis code scanning. Used by"""
    # TODO: implement 'tool/semgrep-sast-proxy'
    return {'received': args, 'tool': 'semgrep-sast-proxy', 'status': 'stub'}


async def _run_opencorporates_lookup(args: dict[str, Any]) -> Any:
    """OpenCorporates company lookup — Look up a company in the OpenCorporates global registry (220M+"""
    # TODO: implement 'tool/opencorporates-lookup'
    return {'received': args, 'tool': 'opencorporates-lookup', 'status': 'stub'}


async def _run_mitre_attack_mapper(args: dict[str, Any]) -> Any:
    """MITRE ATT&CK technique mapper — Map free-text TTPs to MITRE ATT&CK technique IDs (T1234.xxx)."""
    # TODO: implement 'tool/mitre-attack-mapper'
    return {'received': args, 'tool': 'mitre-attack-mapper', 'status': 'stub'}


async def _run_presidio_pii_detect(args: dict[str, Any]) -> Any:
    """Microsoft Presidio PII detection proxy — Proxy to Microsoft Presidio Analyzer for PII detection."""
    # TODO: implement 'tool/presidio-pii-detect'
    return {'received': args, 'tool': 'presidio-pii-detect', 'status': 'stub'}


async def _run_transaction_graph_query(args: dict[str, Any]) -> Any:
    """Transaction graph query — Query a transaction-graph store for one-hop or multi-hop paths"""
    # TODO: implement 'tool/transaction-graph-query'
    return {'received': args, 'tool': 'transaction-graph-query', 'status': 'stub'}


async def _run_google_geocode(args: dict[str, Any]) -> Any:
    """Google Maps Geocoding (address → lat/lng) — Forward and reverse geocoding via Google Maps Geocoding API."""
    # TODO: implement 'tool/google-geocode'
    return {'received': args, 'tool': 'google-geocode', 'status': 'stub'}


async def _run_checklist_evaluator(args: dict[str, Any]) -> Any:
    """Checklist evaluator (GO/NO-GO) — Reads a named procedural checklist (knowledge-pack/technician-checklists record) plus a candidate input, returns per-item disposition (verified|unverified|nogo) + overall verdict (go|nogo). NO-GO triggers override otherwise-clean inputs."""
    # TODO: implement 'processor/checklist-evaluator'
    return {'received': args, 'tool': 'checklist-evaluator', 'status': 'stub'}


async def _run_hyde_query_expander(args: dict[str, Any]) -> Any:
    """HyDE query expander — Hypothetical Document Embeddings (HyDE): generate a hypothetical"""
    # TODO: implement 'processor/hyde-query-expander'
    return {'received': args, 'tool': 'hyde-query-expander', 'status': 'stub'}


async def _run_two_time_retrieval(args: dict[str, Any]) -> Any:
    """Two-time retrieval (refine query, re-retrieve) — Retrieve top-K with the raw query, ask an LLM to compose a refined"""
    # TODO: implement 'processor/two-time-retrieval'
    return {'received': args, 'tool': 'two-time-retrieval', 'status': 'stub'}


async def _run_sub_question_decomposer(args: dict[str, Any]) -> Any:
    """Sub-question decomposer — Break a compound question into N atomic sub-questions, each"""
    # TODO: implement 'processor/sub-question-decomposer'
    return {'received': args, 'tool': 'sub-question-decomposer', 'status': 'stub'}


async def _run_nsfw_image_classifier(args: dict[str, Any]) -> Any:
    """NSFW image classifier — Lightweight NSFW image classifier (CLIP-based zero-shot or a"""
    # TODO: implement 'processor/nsfw-image-classifier'
    return {'received': args, 'tool': 'nsfw-image-classifier', 'status': 'stub'}


async def _run_prompt_injection_detector(args: dict[str, Any]) -> Any:
    """Prompt-injection detector — Detect prompt-injection / jailbreak attempts in user input,"""
    # TODO: implement 'processor/prompt-injection-detector'
    return {'received': args, 'tool': 'prompt-injection-detector', 'status': 'stub'}


async def _run_context_window_packer(args: dict[str, Any]) -> Any:
    """Context-window packer (Lost-in-the-middle aware) — Reorganize retrieved chunks into the model's context window so the"""
    # TODO: implement 'processor/context-window-packer'
    return {'received': args, 'tool': 'context-window-packer', 'status': 'stub'}


async def _run_inject_datetime_locale(args: dict[str, Any]) -> Any:
    """Inject datetime + locale into prompt — Replace placeholders like `{{now}}`, `{{today}}`, `{{user_timezone}}`,"""
    # TODO: implement 'processor/inject-datetime-locale'
    return {'received': args, 'tool': 'inject-datetime-locale', 'status': 'stub'}


async def _run_inject_output_schema(args: dict[str, Any]) -> Any:
    """Inject output schema directive — Render a target JSON Schema (or Pydantic model) into the prompt as"""
    # TODO: implement 'processor/inject-output-schema'
    return {'received': args, 'tool': 'inject-output-schema', 'status': 'stub'}


async def _run_self_refine_critique(args: dict[str, Any]) -> Any:
    """Self-Refine critique loop — Critique-and-revise loop (Madaan et al. 2023). The same model first"""
    # TODO: implement 'processor/self-refine-critique'
    return {'received': args, 'tool': 'self-refine-critique', 'status': 'stub'}


async def _run_llm_judge(args: dict[str, Any]) -> Any:
    """LLM-as-judge — Generic LLM-as-judge wrapper. Given (candidate response, rubric,"""
    # TODO: implement 'processor/llm-judge'
    return {'received': args, 'tool': 'llm-judge', 'status': 'stub'}


async def _run_community_summary_mapreduce(args: dict[str, Any]) -> Any:
    """Community-summary map-reduce (GraphRAG global) — Per-community map step (LLM summarizes each Leiden community), then"""
    # TODO: implement 'processor/community-summary-mapreduce'
    return {'received': args, 'tool': 'community-summary-mapreduce', 'status': 'stub'}


async def _run_multi_vector_fusion(args: dict[str, Any]) -> Any:
    """Multi-vector / multi-query fusion (RRF + weighted) — Fuse N ranked candidate lists from independent retrievers (sparse +"""
    # TODO: implement 'processor/multi-vector-fusion'
    return {'received': args, 'tool': 'multi-vector-fusion', 'status': 'stub'}


async def _run_skeleton_outliner(args: dict[str, Any]) -> Any:
    """Skeleton outliner (Skeleton-of-Thought) — Generate a skeleton (bullet outline) for a long-form output, then"""
    # TODO: implement 'processor/skeleton-outliner'
    return {'received': args, 'tool': 'skeleton-outliner', 'status': 'stub'}


async def _run_intent_dispatcher(args: dict[str, Any]) -> Any:
    """Intent dispatcher — Classify an incoming message into one of N intents and route to the"""
    # TODO: implement 'processor/intent-dispatcher'
    return {'received': args, 'tool': 'intent-dispatcher', 'status': 'stub'}


async def _run_cost_ceiling_gate(args: dict[str, Any]) -> Any:
    """Cost ceiling gate — Reject a pipeline run if the predicted USD cost exceeds the budget"""
    # TODO: implement 'processor/cost-ceiling-gate'
    return {'received': args, 'tool': 'cost-ceiling-gate', 'status': 'stub'}


async def _run_concept_graph_extractor(args: dict[str, Any]) -> Any:
    """Concept graph extractor — Extract typed concept-graph nodes + edges from chunked text. Node types: concept, term, person, dataset, method, equation. Edge types: depends_on, cited_by, sub_concept, contradicts, defined_in. Each node + edge carries a (page, span) source anchor."""
    # TODO: implement 'processor/concept-graph-extractor'
    return {'received': args, 'tool': 'concept-graph-extractor', 'status': 'stub'}


async def _run_redact_pii_text(args: dict[str, Any]) -> Any:
    """Redact PII from text (English-centric, MS Presidio-compatible) — Strip PII from free-form text before downstream LLM calls or"""
    # TODO: implement 'processor/redact-pii-text'
    return {'received': args, 'tool': 'redact-pii-text', 'status': 'stub'}


async def _run_runtime_tool_selector(args: dict[str, Any]) -> Any:
    """Runtime tool selector (Toolformer / pydantic-ai) — Given a user query + a large registry of tools, semantically select"""
    # TODO: implement 'processor/runtime-tool-selector'
    return {'received': args, 'tool': 'runtime-tool-selector', 'status': 'stub'}


async def _run_reasoning_framework_selector(args: dict[str, Any]) -> Any:
    """Reasoning framework selector — Pick a reasoning framework (CoT / ReAct / Tree-of-Thoughts /"""
    # TODO: implement 'processor/reasoning-framework-selector'
    return {'received': args, 'tool': 'reasoning-framework-selector', 'status': 'stub'}


async def _run_persona_set_generator(args: dict[str, Any]) -> Any:
    """Persona-set generator (STORM) — Spawn N personas with distinct perspectives on a topic. Used by"""
    # TODO: implement 'processor/persona-set-generator'
    return {'received': args, 'tool': 'persona-set-generator', 'status': 'stub'}


async def _run_iso_country_normalize(args: dict[str, Any]) -> Any:
    """ISO country code normalize (alpha-2 / alpha-3 / numeric / name) — Resolve any country reference — alpha-2, alpha-3, numeric, English"""
    # TODO: implement 'processor/iso-country-normalize'
    return {'received': args, 'tool': 'iso-country-normalize', 'status': 'stub'}


async def _run_pdf_extract_with_ocr_fallback(args: dict[str, Any]) -> Any:
    """PDF extract with OCR fallback (CiteMind shape) — Extract embedded PDF text page by page; fall back to OCR (Tesseract / PaddleOCR / similar) for pages whose embedded-text yield is below threshold (scanned pages, image-heavy figures)."""
    # TODO: implement 'processor/pdf-extract-with-ocr-fallback'
    return {'received': args, 'tool': 'pdf-extract-with-ocr-fallback', 'status': 'stub'}


async def _run_date_parse_multiformat(args: dict[str, Any]) -> Any:
    """Date parse multi-format → ISO 8601 — Parse any date string in 50+ common formats (MM/DD/YYYY, DD/MM/YYYY,"""
    # TODO: implement 'processor/date-parse-multiformat'
    return {'received': args, 'tool': 'date-parse-multiformat', 'status': 'stub'}


async def _run_address_parse_standardize(args: dict[str, Any]) -> Any:
    """Address parse + standardize (USPS Pub 28 / libpostal) — Parse a free-form postal address into components (street_number,"""
    # TODO: implement 'processor/address-parse-standardize'
    return {'received': args, 'tool': 'address-parse-standardize', 'status': 'stub'}


async def _run_page_aware_chunker(args: dict[str, Any]) -> Any:
    """Page-aware chunker — Split page-extracted text into ~800-token chunks with 120-token overlap; preserve the (page, span) coordinates on every chunk so downstream answers can cite back to the page + span."""
    # TODO: implement 'processor/page-aware-chunker'
    return {'received': args, 'tool': 'page-aware-chunker', 'status': 'stub'}


async def _run_pdf_to_text(args: dict[str, Any]) -> Any:
    """PDF to text — Convert a PDF (extractable layer + optional OCR fallback) into plain"""
    # TODO: implement 'processor/pdf-to-text'
    return {'received': args, 'tool': 'pdf-to-text', 'status': 'stub'}


async def _run_phone_normalize_e164(args: dict[str, Any]) -> Any:
    """Phone number normalize → E.164 (Google libphonenumber) — Parse free-form phone numbers into E.164 international format"""
    # TODO: implement 'processor/phone-normalize-e164'
    return {'received': args, 'tool': 'phone-normalize-e164', 'status': 'stub'}


async def _run_structured_to_prose(args: dict[str, Any]) -> Any:
    """Structured JSON → prose normalizer (for GREP-style rule packs) — Walk a JSON object and emit one prose-like line per leaf value,"""
    # TODO: implement 'processor/structured-to-prose'
    return {'received': args, 'tool': 'structured-to-prose', 'status': 'stub'}


async def _run_name_canonicalize(args: dict[str, Any]) -> Any:
    """Person-name canonicalize (Western + East-Asian) — Canonicalize a person name string into structured components:"""
    # TODO: implement 'processor/name-canonicalize'
    return {'received': args, 'tool': 'name-canonicalize', 'status': 'stub'}


async def _run_audio_to_text_whisper(args: dict[str, Any]) -> Any:
    """Audio to text (Whisper) — Speech-to-text via a Whisper-family model. Returns transcript +"""
    # TODO: implement 'processor/audio-to-text-whisper'
    return {'received': args, 'tool': 'audio-to-text-whisper', 'status': 'stub'}


async def _run_embedder_minilm(args: dict[str, Any]) -> Any:
    """Text embedder (MiniLM-L6-v2) — Generate 384-dimensional text embeddings using"""
    # TODO: implement 'processor/embedder-minilm'
    return {'received': args, 'tool': 'embedder-minilm', 'status': 'stub'}


async def _run_local_embedder(args: dict[str, Any]) -> Any:
    """Local embedder (Ollama / nomic / mxbai) — Embed text chunks via a local embedding model (Ollama nomic-embed-text / mxbai-embed-large / etc.). No network round-trip; embeddings stored locally."""
    # TODO: implement 'processor/local-embedder'
    return {'received': args, 'tool': 'local-embedder', 'status': 'stub'}


async def _run_iterative_revise_loop(args: dict[str, Any]) -> Any:
    """Iterative revise loop — The "send the response back to the LLM with accumulating context" primitive."""
    # TODO: implement 'processor/iterative-revise-loop'
    return {'received': args, 'tool': 'iterative-revise-loop', 'status': 'stub'}


async def _run_llmlingua_context_compressor(args: dict[str, Any]) -> Any:
    """LLMLingua context compressor — Compress long context (retrieved RAG chunks or prior conversation turns)"""
    # TODO: implement 'processor/llmlingua-context-compressor'
    return {'received': args, 'tool': 'llmlingua-context-compressor', 'status': 'stub'}


async def _run_action_sampler_multi_rollout(args: dict[str, Any]) -> Any:
    """Action sampler — N parallel rollouts — Sample N independent action trajectories for an agent task; return"""
    # TODO: implement 'processor/action-sampler-multi-rollout'
    return {'received': args, 'tool': 'action-sampler-multi-rollout', 'status': 'stub'}


async def _run_self_consistency_sampler(args: dict[str, Any]) -> Any:
    """Self-consistency sampler — Run N parallel samples of a chain-of-thought reasoning prompt, then"""
    # TODO: implement 'processor/self-consistency-sampler'
    return {'received': args, 'tool': 'self-consistency-sampler', 'status': 'stub'}


async def _run_hybrid_bm25_vector_retrieve(args: dict[str, Any]) -> Any:
    """Hybrid BM25 + vector retrieve — Combine BM25 lexical scoring with vector cosine similarity (reciprocal rank fusion) for retrieval. Returns top-k chunks with merged ranking, preserving page anchors for citation."""
    # TODO: implement 'processor/hybrid-bm25-vector-retrieve'
    return {'received': args, 'tool': 'hybrid-bm25-vector-retrieve', 'status': 'stub'}


async def _run_cross_encoder_reranker(args: dict[str, Any]) -> Any:
    """Cross-encoder reranker — Re-rank a list of retrieved candidates with a cross-encoder model"""
    # TODO: implement 'processor/cross-encoder-reranker'
    return {'received': args, 'tool': 'cross-encoder-reranker', 'status': 'stub'}


async def _run_entity_resolution_link(args: dict[str, Any]) -> Any:
    """Entity resolution: cluster records into entities — Given N records, cluster those that refer to the same real-world"""
    # TODO: implement 'processor/entity-resolution-link'
    return {'received': args, 'tool': 'entity-resolution-link', 'status': 'stub'}


async def _run_verify_tool_validate_criterion(args: dict[str, Any]) -> Any:
    """Tool-validation success-criterion evaluator — Evaluates one `kind: tool_validate` success criterion. Invokes"""
    # TODO: implement 'processor/verify-tool-validate-criterion'
    return {'received': args, 'tool': 'verify-tool-validate-criterion', 'status': 'stub'}


async def _run_hallucination_scorer(args: dict[str, Any]) -> Any:
    """Hallucination scorer (SelfCheckGPT-style) — Score per-sentence hallucination probability by sampling N alternative"""
    # TODO: implement 'processor/hallucination-scorer'
    return {'received': args, 'tool': 'hallucination-scorer', 'status': 'stub'}


async def _run_verify_composite_criterion(args: dict[str, Any]) -> Any:
    """Composite (AND/OR/NOT) success-criterion evaluator — Evaluates one `kind: composite` success criterion. Combines child"""
    # TODO: implement 'processor/verify-composite-criterion'
    return {'received': args, 'tool': 'verify-composite-criterion', 'status': 'stub'}


async def _run_verify_regex_criterion(args: dict[str, Any]) -> Any:
    """Regex success-criterion evaluator — Evaluates one `kind: regex` success criterion. Given a target"""
    # TODO: implement 'processor/verify-regex-criterion'
    return {'received': args, 'tool': 'verify-regex-criterion', 'status': 'stub'}


async def _run_citation_coverage(args: dict[str, Any]) -> Any:
    """Citation coverage verifier — Verify that every factual sentence in a response carries at least"""
    # TODO: implement 'processor/citation-coverage'
    return {'received': args, 'tool': 'citation-coverage', 'status': 'stub'}


async def _run_official_sources_checker(args: dict[str, Any]) -> Any:
    """Official-sources analyzer — Verify retrieved candidates against an allowlist of authoritative"""
    # TODO: implement 'processor/official-sources-checker'
    return {'received': args, 'tool': 'official-sources-checker', 'status': 'stub'}


async def _run_verify_deterministic_criterion(args: dict[str, Any]) -> Any:
    """Deterministic comparison success-criterion evaluator — Evaluates one `kind: deterministic` success criterion. Resolves a"""
    # TODO: implement 'processor/verify-deterministic-criterion'
    return {'received': args, 'tool': 'verify-deterministic-criterion', 'status': 'stub'}


async def _run_document_grader(args: dict[str, Any]) -> Any:
    """Per-document relevance grader (Self-RAG) — Score each retrieved document for relevance to the user query. Emits"""
    # TODO: implement 'processor/document-grader'
    return {'received': args, 'tool': 'document-grader', 'status': 'stub'}


async def _run_cost_meter(args: dict[str, Any]) -> Any:
    """Cost meter — Emit per-call USD cost accounting given (adapter_ref, input_tokens,"""
    # TODO: implement 'processor/cost-meter'
    return {'received': args, 'tool': 'cost-meter', 'status': 'stub'}


async def _run_json_schema_repair(args: dict[str, Any]) -> Any:
    """JSON Schema repair + validate — Parse and repair JSON inside a model response, then validate against"""
    # TODO: implement 'processor/json-schema-repair'
    return {'received': args, 'tool': 'json-schema-repair', 'status': 'stub'}


async def _run_memory_conversational_store(args: dict[str, Any]) -> Any:
    """Conversational memory store — Read / write conversational memory keyed by (user_id, session_id)."""
    # TODO: implement 'processor/memory-conversational-store'
    return {'received': args, 'tool': 'memory-conversational-store', 'status': 'stub'}


async def _run_recipient_tone_history(args: dict[str, Any]) -> Any:
    """Recipient tone-history loader — Load the user's prior N email / chat exchanges with a specific"""
    # TODO: implement 'processor/recipient-tone-history'
    return {'received': args, 'tool': 'recipient-tone-history', 'status': 'stub'}


async def _run_preference_loader(args: dict[str, Any]) -> Any:
    """User preference loader — Load the user's preference file from"""
    # TODO: implement 'processor/preference-loader'
    return {'received': args, 'tool': 'preference-loader', 'status': 'stub'}


async def _run_calendar_slot_finder(args: dict[str, Any]) -> Any:
    """Calendar slot finder (preference-aware) — Given the user's calendar + their preferences (no-meeting hours,"""
    # TODO: implement 'processor/calendar-slot-finder'
    return {'received': args, 'tool': 'calendar-slot-finder', 'status': 'stub'}


async def _run_recursive_character_chunker(args: dict[str, Any]) -> Any:
    """Recursive character chunker — Split text into chunks using a recursive character splitter"""
    # TODO: implement 'processor/recursive-character-chunker'
    return {'received': args, 'tool': 'recursive-character-chunker', 'status': 'stub'}

HANDLERS = {
    'json-schema-validator': _run_json_schema_validator,
    'cbp-wro-lookup': _run_cbp_wro_lookup,
    'sanctions-check': _run_sanctions_check,
    'swift-bic-validator': _run_swift_bic_validator,
    'txt2img-sdxl': _run_txt2img_sdxl,
    'usps-address-validator': _run_usps_address_validator,
    'web-search': _run_web_search,
    'lookup-icd10': _run_lookup_icd10,
    'semgrep-sast-proxy': _run_semgrep_sast_proxy,
    'opencorporates-lookup': _run_opencorporates_lookup,
    'mitre-attack-mapper': _run_mitre_attack_mapper,
    'presidio-pii-detect': _run_presidio_pii_detect,
    'transaction-graph-query': _run_transaction_graph_query,
    'google-geocode': _run_google_geocode,
    'checklist-evaluator': _run_checklist_evaluator,
    'hyde-query-expander': _run_hyde_query_expander,
    'two-time-retrieval': _run_two_time_retrieval,
    'sub-question-decomposer': _run_sub_question_decomposer,
    'nsfw-image-classifier': _run_nsfw_image_classifier,
    'prompt-injection-detector': _run_prompt_injection_detector,
    'context-window-packer': _run_context_window_packer,
    'inject-datetime-locale': _run_inject_datetime_locale,
    'inject-output-schema': _run_inject_output_schema,
    'self-refine-critique': _run_self_refine_critique,
    'llm-judge': _run_llm_judge,
    'community-summary-mapreduce': _run_community_summary_mapreduce,
    'multi-vector-fusion': _run_multi_vector_fusion,
    'skeleton-outliner': _run_skeleton_outliner,
    'intent-dispatcher': _run_intent_dispatcher,
    'cost-ceiling-gate': _run_cost_ceiling_gate,
    'concept-graph-extractor': _run_concept_graph_extractor,
    'redact-pii-text': _run_redact_pii_text,
    'runtime-tool-selector': _run_runtime_tool_selector,
    'reasoning-framework-selector': _run_reasoning_framework_selector,
    'persona-set-generator': _run_persona_set_generator,
    'iso-country-normalize': _run_iso_country_normalize,
    'pdf-extract-with-ocr-fallback': _run_pdf_extract_with_ocr_fallback,
    'date-parse-multiformat': _run_date_parse_multiformat,
    'address-parse-standardize': _run_address_parse_standardize,
    'page-aware-chunker': _run_page_aware_chunker,
    'pdf-to-text': _run_pdf_to_text,
    'phone-normalize-e164': _run_phone_normalize_e164,
    'structured-to-prose': _run_structured_to_prose,
    'name-canonicalize': _run_name_canonicalize,
    'audio-to-text-whisper': _run_audio_to_text_whisper,
    'embedder-minilm': _run_embedder_minilm,
    'local-embedder': _run_local_embedder,
    'iterative-revise-loop': _run_iterative_revise_loop,
    'llmlingua-context-compressor': _run_llmlingua_context_compressor,
    'action-sampler-multi-rollout': _run_action_sampler_multi_rollout,
    'self-consistency-sampler': _run_self_consistency_sampler,
    'hybrid-bm25-vector-retrieve': _run_hybrid_bm25_vector_retrieve,
    'cross-encoder-reranker': _run_cross_encoder_reranker,
    'entity-resolution-link': _run_entity_resolution_link,
    'verify-tool-validate-criterion': _run_verify_tool_validate_criterion,
    'hallucination-scorer': _run_hallucination_scorer,
    'verify-composite-criterion': _run_verify_composite_criterion,
    'verify-regex-criterion': _run_verify_regex_criterion,
    'citation-coverage': _run_citation_coverage,
    'official-sources-checker': _run_official_sources_checker,
    'verify-deterministic-criterion': _run_verify_deterministic_criterion,
    'document-grader': _run_document_grader,
    'cost-meter': _run_cost_meter,
    'json-schema-repair': _run_json_schema_repair,
    'memory-conversational-store': _run_memory_conversational_store,
    'recipient-tone-history': _run_recipient_tone_history,
    'preference-loader': _run_preference_loader,
    'calendar-slot-finder': _run_calendar_slot_finder,
    'recursive-character-chunker': _run_recursive_character_chunker,
}


async def main() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
