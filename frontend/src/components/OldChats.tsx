export default function OldChats({ clearCurrentChat }: { clearCurrentChat: () => void }) {

    const handleCreateNewChat = () => {
        console.log("hello")
        console.log(typeof clearCurrentChat)
        clearCurrentChat()
    }

    return (
        <div className="w-[25%] bg-[#1B1B1D] flex flex-col justify-start items-center">
            <h2 className="mt-2 font-bold text-4xl text-[#f2f0ef]">Chats</h2>
            <div className="h-full w-full">
                <h2 
                    className="mt-4 mx-5 text-[#f2f0ef] justify-start items-start border-2 border-[#949392] p-1 rounded-lg cursor-pointer"
                    onClick={handleCreateNewChat}
                >
                   Create a new Chat 💻 
                </h2>
                <h2 className="mt-4 mx-5 text-[#f2f0ef] justify-start items-start border-2 border-[#949392] p-1 rounded-lg cursor-pointer">
                    Current Chat 📜
                </h2>
            </div>
        </div>
    )
}
