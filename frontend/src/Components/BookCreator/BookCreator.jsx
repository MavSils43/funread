import React from 'react'
import './BookCreator.css'
import NavbarButtons from '../Shared/NavbarButtons/NavbarButtons'
import Sidebar from '../Shared/Sidebar/Sidebar'
import Carousel from '../Shared/NavBarCarrousel/NavBarCarrousel'
import PageContainer from '../Shared/PageContainer/PageContainer'

const BookCreator = () => {
  return (
    <>
      <div className='container-fluid p-0'>
        <div className='row flex-nowrap'>
          <Sidebar />
          <div className='col-md-10 p-0' style={{ width: '100%' }}>
            <div className='p-0'>
              <NavbarButtons />
              <Carousel />
              <PageContainer
                title={'Activity 3'}
                image={
                  'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg'
                }
                width={'300'}
                height={'300'}
                imageAlt={'landscape'}
                text={'Text'}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default BookCreator
