import { type Point, type TextWidth } from "./diagram-model.js";
/**
 * The model and layout behind a `Sequence`: the actor and message props and
 * where each header, lifeline, arrow, label, and note sits for a block of a
 * given width. Pure, no React.
 */
export interface SequenceActor {
    /** Unique id, the one messages name in `from`, `to`, and `over`. */
    id: string;
    /** The actor's name in its header box. Wraps to two lines, then ends in an ellipsis. */
    label: string;
    /** A second, smaller line under the label: a role, a service, a host. One line, cut with an ellipsis. */
    detail?: string;
}
export interface SequenceMessage {
    /** Id of the actor the arrow leaves. */
    from: string;
    /** Id of the actor the arrow points to; the same as `from` draws a self-call loop with its label to the right. */
    to: string;
    /** Short text above the arrow: a call, an event, a status. Wraps to two lines, then ends in an ellipsis. */
    label?: string;
    /** A return: drawn dashed in the gray `other` instead of solid in the first data color. */
    reply?: boolean;
}
export interface SequenceNote {
    /** The note's text, in a tinted box on its own row. Wraps to three lines, then ends in an ellipsis. */
    note: string;
    /** Id of the actor the note sits over. Absent, it spans every actor; an unknown id skips the note. */
    over?: string;
}
/** A row of a `Sequence`, top to bottom: a message arrow or a note. */
export type SequenceRow = SequenceMessage | SequenceNote;
export interface SequenceProps {
    /** The actors, one column each, left to right. Duplicate ids keep the first; an empty list draws nothing. */
    actors: SequenceActor[];
    /** The rows, top to bottom. A message naming an unknown actor id is skipped; an empty list draws the actors and their lifelines alone. */
    messages: SequenceRow[];
}
