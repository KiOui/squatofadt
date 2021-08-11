export default function getEnvVar(name: string): string {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  if (window?.__env__?.[name]) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    return window?.__env__?.[name];
  } else if (process.env[name]) {
    return process.env[name];
  } else {
    throw new Error(`Environment variable ${name} is not defined.`);
  }
}
