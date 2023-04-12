import { Routes, Route } from 'react-router-dom';
import { GlobalStyles } from './styles/GlobalStyles';
import LoginPage from './pages/LoginPage';
import PersonaChoice from './pages/PersonaChoicePage';
import MyPostsPage from './pages/MyPostsPage';
import PostDetailPage from './pages/PostDetailPage';
import BackgroundLayout from './components/commons/BackgroundLayout';

const App = () => {
  return (
    <BackgroundLayout>
      <GlobalStyles />
      <Routes>
        <Route path='/' element={<LoginPage />} />
        <Route path='/personas' element={<PersonaChoice />} />
        <Route path='/posts' element={<MyPostsPage />} />
        <Route path='/posts/:id' element={<PostDetailPage />} />
      </Routes>
    </BackgroundLayout>
  );
}

export default App;