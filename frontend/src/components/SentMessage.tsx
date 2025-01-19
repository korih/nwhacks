interface SentMessageProps {
    msg: string;
}

export default function SentMessage({ msg }: SentMessageProps) {
    return (
        <div className="items-end flex justify-end">
            <div className="bg-[#c9c8c7] mt-2 px-2 py-2 w-fit rounded-lg items-end max-w-[80%] break-words">
                <span className="text-[#010000]">
                    {msg}
                </span>
            </div>
        </div>
    )
}
