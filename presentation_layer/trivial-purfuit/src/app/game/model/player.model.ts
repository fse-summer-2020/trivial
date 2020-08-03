export interface Player {
    name: string,
    color: string,
    collected_wedges?: any[],
    location?: number[][],
    winning_condition?: boolean,
    player_name?: string
}