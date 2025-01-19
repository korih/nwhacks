import { useEffect, useState } from "react";
import Header from "../components/Header";
import ReceivedMessage from "../components/ReceivedMessage";
import SentMessage from "../components/SentMessage";
import OldChats from "../components/OldChats";
import { useLocation } from "react-router-dom";
import axios from "axios";

export default function Chatter() {
    const URL = "http://127.0.0.1:8000/api/chat"

    const location = useLocation();
    const { query } = location.state || {};
    const [receivedMessages, setReceivedMessages] = useState<any>([]);
    const [sentMessages, setSentMessages] = useState<any>([]);
    const [currentMessage, setCurrentMessage] = useState('');
    const [messages, setMessages] = useState<any>([]);
    //    const [chats, setChats] = useState([]);


    const handleSendMessage = async (msg: string) => {
        // sent the message to backend
        // handle setting the set messages

        try {
            console.log('sent')
            const response_raw = await axios.post(URL, { "role": "user", "content": msg })
            if (response_raw.status === 200) {
                const response = response_raw.data.message.result.response
                console.log(response)
                const recMsg = { "msg": response, "type": "received" };
                const sentMsg = { "msg": msg, "type": "sent" }
                setReceivedMessages((old: any) => [...old, recMsg]);
                setSentMessages((old: any) => [...old, sentMsg]);
                setMessages((old: any) => [...old, sentMsg])
                setMessages((old: any) => [...old, recMsg])
            }
        } catch (err) {
            alert(`Error in sending: ${err}`)
        }
    }

    const handleKeyDown = (e: any) => {
        if (e.key === 'Enter' && currentMessage.length > 0) {
            handleSendMessage(currentMessage);
            setCurrentMessage('')
        }
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
                    <div id="container-for-chat" className="m-10 h-[50%] overflow-y-scroll">
                        {messages.map((msg: any) => (
                            msg.type === 'received' ? (
                                <ReceivedMessage msg={msg.msg} />
                            ) : (
                                <SentMessage msg={msg.msg} />
                            )
                        ))}
                    </div>
                    <div id="For chat bar">

                        <div className="w-[100%] flex justify-center">
                            <input
                                type="text"
                                className="break-words whitespace-normal bg-[#949392] px-5 w-full h-10 rounded-3xl flex justify-center m-10 max-=-[100%]"
                                onKeyDown={handleKeyDown}
                                value={currentMessage}
                                onChange={(e) => setCurrentMessage(e.target.value)}
                            />
                        </div>
                    </div>
                    <div>

                    </div>
                </section>
            </div>
        </div>
    )
}
