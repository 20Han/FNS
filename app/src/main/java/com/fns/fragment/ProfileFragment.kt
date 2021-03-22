package com.fns.fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.fns.databinding.FragmentProfileBinding

class ProfileFragment : Fragment(){
    private var mBinding : FragmentProfileBinding? = null

     override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        mBinding = FragmentProfileBinding.inflate(inflater, container, false)
        return mBinding?.root
    }

    override fun onDestroyOptionsMenu() {
        mBinding = null
        super.onDestroyOptionsMenu()
    }
}