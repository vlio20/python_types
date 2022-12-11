type MetricTag = `${string}:${string}`;

const validationCntr: MetricTag = 'validationPassed:success';

// Type '"validationPassed_success"' is not assignable to type '`${string}:${string}`'.
const validationCntr2: MetricTag = 'validationPassed_success';