import React from 'react'

function OptimizationSection({ optimizations }) {
    return (
        <div className='mt-10 max-w-2xl'>
            {optimizations && optimizations.length > 0 && (
                <div className='bg-purple-100 border border-purple-400 text-purple-700 px-4 py-3 rounded relative' role='alert'>
                    <strong className='font-bold'>optimization!</strong>
                    <ul>
                        {optimizations.map((optimization, index) => (
                            <li key={index}>➡️{optimization}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default OptimizationSection