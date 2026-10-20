// 统一识别慢网、节省数据与减少动态效果偏好。
const connection=navigator.connection;
export const slowNetwork=Boolean(connection?.saveData||/2g|3g/.test(connection?.effectiveType||''));
export const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
export const narrowScreen=()=>matchMedia('(max-width: 899px)').matches;
