import { useNavigate } from "react-router-dom"

export default function Header() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate('/home')
  }

  return (
    <section 
      className="h-32 w-full fixed top-0 left-0 bg-[#66615e]"
      onClick={handleClick}
    >
      <div className="flex justify-center mt-7 cursor-pointer">
        <h1 className="font-bold text-7xl">Chatza</h1>
      </div>
    </section>
  )
}
