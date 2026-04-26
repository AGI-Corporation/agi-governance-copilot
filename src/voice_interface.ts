import { createGoogleGenerativeAI } from '@ai-sdk/google';
import { VoiceSession } from 'bodhi-realtime-agent';

/**
 * AGI Governance Copilot - Voice Interface
 * Powered by Bodhi Realtime Agent
 * 
 * This module connects the high-performance Bodhi voice stack to the 
 * AGI Governance OpenClaw gateway for real-time, non-blocking 
 * fiduciary oversight and decision-making.
 */

const session = new VoiceSession({
  sessionId: `agi-gov-${Date.now()}`,
  userId: 'steward_1',
  apiKey: process.env.GOOGLE_API_KEY!,
  agents: [
    {
      name: 'M.I.K.E.',
      instructions: `You are M.I.K.E. (Master Intelligence & Knowledge Executive), 
       the primary voice interface for the AGI Governance Copilot. 
       Your role is to assist human stewards in evaluating proposals 
       and monitoring the Governance Ledger in real-time. 
       Be concise, fiduciary-minded, and transparent.`,
      tools: [
        {
          name: 'evaluate_proposal',
          description: 'Evaluate a governance proposal against the Institutional Grid.',
          execution: 'background', // Non-blocking background task
          execute: async (args) => {
            // Communicate with the OpenClaw gateway
            const response = await fetch('http://localhost:18789/evaluate', {
              method: 'POST',
              body: JSON.stringify(args)
            });
            return await response.json();
          }
        },
        {
          name: 'check_governance_ledger',
          description: 'Retrieve the latest entries from the tamper-evident ledger.',
          execution: 'inline',
          execute: async () => {
            const response = await fetch('http://localhost:18789/ledger/latest');
            return await response.json();
          }
        }
      ]
    }
  ],
  initialAgent: 'M.I.K.E.',
  port: 9900,
  model: createGoogleGenerativeAI({
    apiKey: process.env.GOOGLE_API_KEY!
  })('gemini-2.5-flash'),
});

session.start().then(() => {
  console.log('🎙️ AGI Governance Voice Interface active on ws://localhost:9900');
});
