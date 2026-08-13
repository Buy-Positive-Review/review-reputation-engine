#!/usr/bin/env node

interface ReputationEngineInput {
  brand: string;
  platform: string;
  reviewVisibility: number;
  reputationHealth: number;
  feedbackPattern: number;
  platformCoverage: number;
  responseRate: number;
  brandPresence: number;
}

interface ReputationEngineOutput {
  brand: string;
  platform: string;
  reviewVisibilityScore: number;
  reputationHealthScore: number;
  feedbackPatternScore: number;
  platformCoverageScore: number;
  responseRateScore: number;
  brandPresenceScore: number;
  overallReputationIndex: number;
  priorityAction: string;
  reviewPlatforms: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    reviewVisibility: "Review Visibility",
    reputationHealth: "Reputation Health",
    feedbackPattern: "Feedback Pattern",
    platformCoverage: "Platform Coverage",
    responseRate: "Response Rate",
    brandPresence: "Brand Presence",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getReviewPlatforms(visibility: number, health: number, coverage: number, brand: number): Record<string, number> {
  return {
    "Google": Math.min(100, Math.round(visibility * 1.0)),
    "Trustpilot": Math.min(100, Math.round(health * 1.0)),
    "Yelp": Math.min(100, Math.round(coverage * 1.0)),
    "App Stores": Math.min(100, Math.round(brand * 1.0)),
  };
}

export function runReputationEngine(input: ReputationEngineInput): ReputationEngineOutput {
  const scores = {
    reviewVisibility: input.reviewVisibility,
    reputationHealth: input.reputationHealth,
    feedbackPattern: input.feedbackPattern,
    platformCoverage: input.platformCoverage,
    responseRate: input.responseRate,
    brandPresence: input.brandPresence,
  };
  const overallReputationIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    platform: input.platform.charAt(0).toUpperCase() + input.platform.slice(1),
    reviewVisibilityScore: input.reviewVisibility,
    reputationHealthScore: input.reputationHealth,
    feedbackPatternScore: input.feedbackPattern,
    platformCoverageScore: input.platformCoverage,
    responseRateScore: input.responseRate,
    brandPresenceScore: input.brandPresence,
    overallReputationIndex,
    priorityAction: getPriorityAction(scores),
    reviewPlatforms: getReviewPlatforms(input.reviewVisibility, input.reputationHealth, input.platformCoverage, input.brandPresence),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const platform = args[1] || "google";
const reviewVisibility = parseInt(args[2]) || 88;
const reputationHealth = parseInt(args[3]) || 82;
const feedbackPattern = parseInt(args[4]) || 85;
const platformCoverage = parseInt(args[5]) || 78;
const responseRate = parseInt(args[6]) || 90;
const brandPresence = parseInt(args[7]) || 84;

const result = runReputationEngine({
  brand, platform, reviewVisibility, reputationHealth,
  feedbackPattern, platformCoverage, responseRate, brandPresence,
});

console.log(`Brand: ${result.brand}`);
console.log(`Platform: ${result.platform}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Review Visibility Score:       ${result.reviewVisibilityScore}/100  [${getStatus(result.reviewVisibilityScore)}]`);
console.log(`Reputation Health Score:       ${result.reputationHealthScore}/100  [${getStatus(result.reputationHealthScore)}]`);
console.log(`Feedback Pattern Score:        ${result.feedbackPatternScore}/100  [${getStatus(result.feedbackPatternScore)}]`);
console.log(`Platform Coverage Score:       ${result.platformCoverageScore}/100  [${getStatus(result.platformCoverageScore)}]`);
console.log(`Response Rate Score:           ${result.responseRateScore}/100  [${getStatus(result.responseRateScore)}]`);
console.log(`Brand Presence Score:          ${result.brandPresenceScore}/100  [${getStatus(result.brandPresenceScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Reputation Index:      ${result.overallReputationIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nReview Platforms:");
Object.entries(result.reviewPlatforms).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(22)} ${score}/100`);
});
