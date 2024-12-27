import { fly, fade, slide } from 'svelte/transition';
import { elasticOut, cubicOut } from 'svelte/easing';

export const pageTransition = {
  in: { 
    duration: 700,
    delay: 300,
    y: 50,
    opacity: 0,
    easing: cubicOut
  },
  out: { 
    duration: 300,
    y: -50,
    opacity: 0
  }
};

export const cardAnimation = (i) => ({
  y: 50,
  duration: 800,
  delay: i * 100,
  opacity: 0,
  easing: elasticOut
});

export const pulseAnimation = `
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }
`;

export const gradientAnimation = `
  @keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
`;

export const floatAnimation = `
  @keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
  }
`;

export const staggerDelay = (index) => index * 100; 