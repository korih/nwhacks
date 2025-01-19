import { useState } from "react";
import Header from "../components/Header";
import ReceivedMessage from "../components/ReceivedMessage";
import SentMessage from "../components/SentMessage";
import OldChats from "../components/OldChats";

export default function Chatter() {
    const [receivedMessages, setReceivedMessages] = useState([]);
    const [sentMessages, setSentMessages] = useState([]);
    const [chats, setChats] = useState([]);
    const [currentMessage, setCurrentMessage] = useState('');

    const handleSendMessage = () => {
        // sent the message to backend
        // handle setting the set messages
    }

    const handleReceiveMessage = () => {
        // handle receiving the message
        // set the received message to state
    }

    const handleReceiveOldChats = () => {
        // handle the get request for old chats
    }

    // should make a container for body and context window
    return (
        <div className="w-full h-full fixed top-32">
            <Header />
            <div className="flex w-full h-full">
                <OldChats />
                <section className="w-full h-full flex flex-col">
                    <div id="container-for-chat" className="m-10 h-[50%]">
                        <ReceivedMessage
                            msg="message"
                        />
                        <SentMessage
                            msg="message"
                        />
                    </div>
                    <div id="For chat bar">

                        <div className="w-[100%] flex justify-center">
                            <input type="text" className="break-words whitespace-normal bg-[#949392] px-5 w-full h-10 rounded-3xl flex justify-center m-10 max-w-[100%]" />
                        </div>
                    </div>
                    <div>

                    </div>
                </section>
            </div>
        </div>
    )
}
