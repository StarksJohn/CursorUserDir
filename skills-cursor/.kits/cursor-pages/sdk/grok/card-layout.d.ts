import { type JSX, type ReactNode } from "react";
export interface CardCarouselProps {
    /** The cards in order, the one you recommend first: two to six `ProductCard`s. */
    children: ReactNode;
    /** What the cards are, for a screen reader: `"Bedside lamps"`, `"Places for Saturday"`. */
    label?: string;
}
/**
 * A handful of items, one card each, standing in a list: one a row, and two
 * a row where both get 320 px, a lone last card centered at a column's
 * width, every card in a row the tallest one's height. Each card keeps
 * every photo it brings, swiping through them on its own, with its facts
 * and its choice on it. The cards never scroll sideways. No cards draws
 * nothing.
 *
 * @kitUnlisted Only a host whose prompt lays out consumer pages teaches it.
 */
export declare function CardCarousel(props: CardCarouselProps): JSX.Element | null;
export interface CardGridProps {
    /** The cards in order: six or more `ProductCard`s with `compact`. */
    children: ReactNode;
    /** What the cards are, for a screen reader: `"Lamps under $500"`. */
    label?: string;
}
/**
 * Many cards seen at once: two a row on a phone, three or four on a wider
 * frame, scrolling down with the page. Every card in a row takes the tallest
 * one's height and the gaps are even. Made for `ProductCard`s with `compact`,
 * which stay readable at half a phone's width. No cards draws nothing.
 *
 * @kitUnlisted Only a host whose prompt lays out consumer pages teaches it.
 */
export declare function CardGrid(props: CardGridProps): JSX.Element | null;
