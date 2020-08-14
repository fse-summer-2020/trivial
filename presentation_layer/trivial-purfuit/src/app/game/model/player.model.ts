import { Category } from './category.model';

export interface Player {
    name: string,
    color: string,
    collected_wedges?: Category[],
    location?: any[],
    winning_condition?: boolean,
    player_name?: string
}