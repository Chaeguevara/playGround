export type VNode = {
  type: string;
  props: Record<string, any>;
  children: VNode[];
};
